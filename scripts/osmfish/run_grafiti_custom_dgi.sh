#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=osm_grafiti
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=output/%j.output
#SBATCH --error=error/%j.error
##################################

python osmfish_grafiti_custom_dgi.py
