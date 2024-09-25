#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=osmfish_distribution
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=osmfish_distribution.output
#SBATCH --error=osmfish_distribution.error
##################################

python osmfish_grafiti_distribution.py
