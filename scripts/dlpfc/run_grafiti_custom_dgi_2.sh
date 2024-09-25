#!/bin/bash

#SBATCH --partition=componc_gpu
#SBATCH --job-name=custom2_dgi
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus=1
#SBATCH --mem=50G
#SBATCH --output=custom2_dgi.output
#SBATCH --error=custom2_dgi.error
##################################

python dlpfc_grafiti_custom_dgi_2.py
