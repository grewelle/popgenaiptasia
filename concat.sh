#!/bin/bash
#
#SBATCH --job-name=concat
#SBATCH --partition=dev
#SBATCH --mem=4G


for sample in `ls ./fastqs/florida/s300-399/*_L001_M_out_001.fastq`
do
dir="./fastqs/florida/s300-399"
base=$(basename $sample "_L001_M_out_001.fastq")
cat ${dir}/${base}_L001_M_out_001.fastq ${dir}/${base}_L002_M_out_001.fastq > ${dir}/${base}_all.fastq
done
