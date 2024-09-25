#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=osmfish_norm
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=osmfish_grafiti.output
#SBATCH --error=osmfish_grafiti.error
##################################

python osmfish_grafiti.py
