#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=custom_graphcl
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=custom_graphcl.output
#SBATCH --error=custom_graphcl.error
##################################

python dlpfc_grafiti_custom_graphcl.py
