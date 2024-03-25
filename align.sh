#!/bin/bash
#
#SBATCH --job-name=align3b
#SBATCH --partition=normal
#SBATCH --mem=4G
#SBATCH --output=R-%x.%j.out
#SBATCH --error=R-%x.%j.err

ml biology
ml bowtie2

for sample in `ls ./fastqs/florida/s200-299/extra/*all.fastq`
do
dir="./fastqs/florida/s200-299/extra"
base=$(basename $sample ".fastq")
bowtie2 -q -x /scratch/users/regrew/bowtieIndices/index -U ${dir}/${base}.fastq -S ${dir}/${base}.sam
done
