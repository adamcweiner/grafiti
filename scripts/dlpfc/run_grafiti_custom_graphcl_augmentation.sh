#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=node
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=100G
#SBATCH --output=output/%j.output
#SBATCH --error=error/%j.error
##################################

python dlpfc_grafiti_custom_graphcl_augmentation.py
