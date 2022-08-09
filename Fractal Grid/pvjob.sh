#!/bin/bash
#SBATCH -N 1
#SBATCH -t 23:30:00
#SBATCH -J python_script 
#SBATCH -A k1093

echo "start:"
date

module load paraview

#module use /sw/vis/xc40.modules
#module load ParaView/5.4.1-CrayGNU-2016.07.KSL-server-mesa

############### DO YOUR WORK HERE ########################
 
srun -n 32 pvbatch overlinex.py
srun -n 32 pvbatch overliney.py
################# YOUR WORK ENDS #########################


echo "finish:"
date
