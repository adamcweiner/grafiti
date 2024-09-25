#!/bin/bash

#SBATCH --partition=componc_cpu
#SBATCH --job-name=osmfish_graphst
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G
#SBATCH --output=osmfish_graphst.output
#SBATCH --error=osmfish_graphst.error
##################################

python osmfish_graphst.py
