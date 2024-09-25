#!/bin/bash

#SBATCH --partition=componc_cpu
#SBATCH --job-name=graphst
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=50G
#SBATCH --output=graphst.output
#SBATCH --error=graphst.error
##################################

python dlpfc_graphst.py
