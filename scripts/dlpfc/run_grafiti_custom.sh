#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=dlpfc_custom
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=dlpfc_custom.output
#SBATCH --error=dlpfc_custom.error
##################################

python dlpfc_grafiti_custom.py
