#!/bin/bash

#SBATCH --partition=componc_cpu
#SBATCH --job-name=osmfish_stagate
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G
#SBATCH --output=osmfish_stagate.output
#SBATCH --error=osmfish_stagate.error
##################################

python osmfish_stagate.py
