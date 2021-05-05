#!/bin/bash --login
#SBATCH --time 2:00:00
#SBATCH --cpus-per-task=4  
#SBATCH --mem-per-cpu=9G 
#SBATCH --constraint=intel
#SBATCH --partition=batch 
#SBATCH --mail-type=ALL
#SBATCH --output=results/%x/%j-slurm.out
#SBATCH --error=results/%x/%j-slurm.err

# entire script fails if single command fails
set -e

# activate the conda environment
module purge
ENV_PREFIX=$PROJECT_DIR/env
conda activate $ENV_PREFIX

# launch the training script
python $1
