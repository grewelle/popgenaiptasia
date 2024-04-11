#!/bin/bash
#
#SBATCH --job-name=markDups
#SBATCH --partition=normal
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --output=R-%x.%j.out
#SBATCH --error=R-%x.%j.err

ml biology
ml gatk

for sample in `ls ./fastqs/hawaii/outgroupSam/*_sorted.bam`
do
dir="./fastqs/hawaii/outgroupSam"
base=$(basename $sample "_sorted.bam")
gatk MarkDuplicatesSpark -I ${dir}/${base}_sorted.bam -O ${dir}/${base}_markDup.bam -M ${dir}/${base}_markDup.txt
done
