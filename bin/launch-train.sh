#!/bin/bash

# entire script fails if a single command fails
set -e

# script should be run from the project directory
export PROJECT_DIR=$PWD

# creates a separate directory for each job
JOB_NAME=example-training-job
mkdir -p $PROJECT_DIR/results/$JOB_NAME

# launch the training job
sbatch --job-name $JOB_NAME $PROJECT_DIR/bin/train.sbatch $PROJECT_DIR/src/train.py 

