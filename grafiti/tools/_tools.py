import umap as umap_ext
import scanpy as sc
from sklearn.manifold import TSNE
import networkx as nx
import math
import numpy as np
import collections
import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.metrics import davies_bouldin_score
import seaborn as sns

grafiti_colors = [
    "#272822",  # Background
    "#F92672",  # Red
    "#FD971F",  # Orange
    "#E6DB74",  # Yellow
    "#A6E22E",  # Green
    "#66D9EF",  # Blue
    "#AE81FF",  # Purple
    "#75715E",  # Brown
    "#F92659",  # Pink
    "#D65F0E",  # Abricos
    "#1E1E1E",   # Black
    "#004d47",  # Darker Teal
    "#D291BC",  # Soft Pink
    "#3A506B",  # Dark Slate Blue
    "#5D8A5E",  # Sage Green
    "#A6A1E2",  # Dull Lavender
    "#E97451",  # Burnt Sienna
    "#6C8D67",  # Muted Lime Green
    "#832232",  # Dim Maroon
    "#669999",  # Desaturated Cyan
    "#C08497",  # Dusty Rose
    "#587B7F",  # Ocean Blue
    "#9A8C98",  # Muted Purple
    "#F28E7F",  # Salmon
    "#F3B61F",  # Goldenrod
    "#6A6E75",  # Iron Gray
    "#FFD8B1",  # Light Peach
    "#88AB75",  # Moss Green
    "#C38D94",  # Muted Rose
    "#6D6A75",  # Purple Gray
]

def degree_distribution(G):
    vk = dict(G.degree())
    vk = list(vk.values()) # we get only the degree values
    maxk = np.max(vk)
    mink = np.min(min)
    kvalues= np.arange(0,maxk+1) # possible values of k
    Pk = np.zeros(maxk+1) # P(k)
    for k in vk:
        Pk[k] = Pk[k] + 1
    Pk = Pk/sum(Pk) # the sum of the elements of P(k) must to be equal to one
    return kvalues,Pk

def shannon_entropy(G):
    k,Pk = degree_distribution(G)
    H = 0
    for p in Pk:
        if(p > 0):
            H = H - p*math.log(p, 2)
    return H

def umap(adata, encoding_key="X_grafiti",n_neighbors=20,max_iter=100, min_dist=0.5, metric="euclidean", scanpy=False, neighbors_key="grafiti_neighbors"):
    if not scanpy:
        ldm = umap_ext.UMAP(n_epochs=max_iter,
                        n_neighbors=n_neighbors,
                        min_dist=min_dist,
                        metric=metric)
        embd = ldm.fit_transform(adata.obsm[encoding_key])
        adata.obsm["X_umap"] = embd
    else:
        sc.tl.umap(adata,neighbors_key=neighbors_key)
    

def find_motifs(adata, resolution=0.5, cluster_key="grafiti_motif", neighbor_method="umap", n_neighbors=50, prefix="GrafitiMotif", encoding_key="X_grafiti",method="louvain",metric="euclidean",k=10,max_iter=10,use_weights=False, compute_neighbors=True):
    if compute_neighbors:
        sc.pp.neighbors(adata,use_rep=encoding_key,key_added="grafiti_neighbors", n_neighbors=n_neighbors, method=neighbor_method, metric=metric)
    if method == "louvain":
        sc.tl.louvain(adata,resolution=resolution,key_added=cluster_key,neighbors_key="grafiti_neighbors",use_weights=use_weights)
    elif method == "leiden":
        sc.tl.leiden(adata,resolution=resolution,key_added=cluster_key,neighbors_key="grafiti_neighbors",use_weights=use_weights)
    elif method == "gm":
        gm = GaussianMixture(n_components=k, random_state=0, max_iter=max_iter).fit(adata.obsm[encoding_key])
        adata.obs[cluster_key] = ["{}{}".format(prefix,x) for x in gm.predict(adata.obsm[encoding_key]).tolist()]
    else:
        raise ValueError("Method should be Louvain or Leiden.")
    adata.obs[cluster_key] = ["{}{}".format(prefix,x) for x in adata.obs[cluster_key].tolist()]

def get_fov_graph(adata, fov_id, fov_key="sample_fov"):
    sub = adata[adata.obs[fov_key]==fov_id]
    G = nx.from_numpy_array(sub.obsp["spatial_connectivities"])
    return G

def fov_entropy(adata, fov_id, fov_key="sample_fov"):
    G = get_fov_graph(adata,fov_id,fov_key=fov_key)
    return shannon_entropy(G)

def depth(adata,fov_key="sample_fov",key_added="depth"):
    onion_map = dict()
    for fovid in set(adata.obs[fov_key]): 
        G = get_fov_graph(adata,fovid,fov_key=fov_key)
        onion_layers = nx.onion_layers(G)
        sub = adata[adata.obs[fov_key] == fovid]
        for i, bc in enumerate(sub.obs.index):
            onion_map[bc] = onion_layers[i]
    onion_layer = []
    for bc in adata.obs.index:
        onion_layer.append(onion_map[bc])
    adata.obs[key_added] = onion_layer

def count_edges(adata):
    G = nx.from_numpy_array(adata.obsp["spatial_connectivities"])
    cts = adata.obs["sap"].tolist()
    count_edges = collections.defaultdict(lambda : collections.defaultdict(int))
    for e in G.edges():
        n1 = cts[e[0]]
        n2 = cts[e[1]]
        count_edges[n1][n2] += 1
        count_edges[n2][n1] += 1
    matrix = []
    saps = list(set(adata.obs["GrafitiMotif"]))
    for s1 in saps:
        row = []
        for s2 in saps:
            row.append(count_edges[s1][s2])
        matrix.append(row)
    data = pd.DataFrame(data=np.array(matrix),index= saps,columns=saps)
    return data

def find_optimal_clustering(adata, low_res, high_res, number_of_points, metric="dbi",encoding_key='X_grafiti',plot=True):
    resolutions = np.linspace(low_res, high_res, number_of_points)
    dbis = []
    keys = []
    for i in resolutions:
        cluster_key = "GrafitiMotif_{}".format(i)
        gf.tl.find_motifs(adata, resolution=i, cluster_key=cluster_key, compute_neighbors=False)
        keys.append(cluster_key)
        dbi = davies_bouldin_score(adata.obsm[encoding_key], adata.obs[cluster_key])
        dbis.append(dbi)
    df = pd.DataFrame.from_dict({"Resolution":resolutions,"DBI":dbis})
    if plot:
        sns.plot(data=df,x="Resolution",y="DBI")
    best_result = resolutions[np.argmin(dbis)]
    return best_result
