#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=graphst_s
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=graphst_s.output
#SBATCH --error=graphst_s.error
##################################

python osmfish_graphst_s.py
