#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=dgi_pca
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=output/%j.output
#SBATCH --error=error/%j.error
##################################

python dlpfc_grafiti_custom2_dgi.py
