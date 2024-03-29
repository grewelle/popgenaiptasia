#!/bin/bash
#
#SBATCH --job-name=indexBam
#SBATCH --partition=normal
#SBATCH --mem=16G
#SBATCH --output=R-%x.%j.out
#SBATCH --error=R-%x.%j.err

ml biology
ml gatk
ml samtools

for sample in `ls ./fastqs/hawaii/outgroupSam/*_sorted.bam`
do
dir="./fastqs/hawaii/outgroupSam"
base=$(basename $sample "_sorted.bam")
samtools index ${dir}/${base}_sorted.bam
done
