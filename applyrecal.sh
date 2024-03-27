#!/bin/bash
#
#SBATCH --job-name=applyrecal_all
#SBATCH --partition=normal
#SBATCH --mem=64G
#SBATCH --time=10:00:00
#SBATCH --output=R-%x.%j.out
#SBATCH --error=R-%x.%j.err

ml biology
ml gatk

for sample in `ls ./fastqs/all/aipSam/*_markDup.bam`
do
dir="./fastqs/all/aipSam"
base=$(basename $sample "_markDup.bam")
gatk --java-options "-Xmx64g" ApplyBQSR -R bowtieIndices/aipGenomeConcat.fna -I ${dir}/${base}_markDup.bam --bqsr-recal-file ${dir}/${base}_recal.table -O ${dir}/${base}_recal.bam
done
