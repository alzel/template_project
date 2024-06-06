#!/bin/bash

#SBATCH --time 48:00:00
#SBATCH --ntasks 64

#module load GCC/8.3.0 iccifort/2019.5.281 CUDA/10.1.168
module load GCC/8.3.0  CUDA/10.1.243  OpenMPI/3.1.4 


CMD=$*

date
hostname
echo "Command:" $CMD

time singularity exec --nv container.sif python ${CMD}