#!/bin/bash --login

# create the conda environment
PROJECT_DIR=$PWD
ENV_PREFIX=$PROJECT_DIR/env
conda env create --prefix $ENV_PREFIX --file $PROJECT_DIR/environment.yml --force
