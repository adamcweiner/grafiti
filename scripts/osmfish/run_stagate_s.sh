#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=stagate_s
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=osmfish_stagate_s.output
#SBATCH --error=osmfish_stagate_s.error
##################################

python osmfish_stagate_s.py
