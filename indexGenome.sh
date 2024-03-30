#!/bin/bash
#
#SBATCH --job-name=indexGenome
#SBATCH --partition=dev
#SBATCH --mem=16G

ml biology
ml bowtie2

bowtie2-build ./aipGenomeConcat.fna index
