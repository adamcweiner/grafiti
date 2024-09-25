#!/bin/bash

#SBATCH --partition=componc_cpu
#SBATCH --job-name=stagate
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G
#SBATCH --output=stagate.output
#SBATCH --error=stagate.error
##################################

python dlpfc_stagate.py
