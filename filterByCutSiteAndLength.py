"""
Takes in fastq file from NovaSeq and returns fastq file with only 36 nt reads and bcg1 cut sites
Also returns statistics for percent with wrong length, wrong cut sites
8-14-23
Richard Grewelle
"""
import gzip #to stream gzipped files
import os #to walk through file tree
from itertools import islice

def load(file):
    countCorrect = 0 #initiate counts for read errors
    countWrongLength = 0
    countBCGmiss = 0
    countWrongSite = 0
    fileOut = file[:-3]  #convert to fastq file
    with gzip.open(file, "r") as f: #read in gzip fastq files
        with open(fileOut, 'w') as f2: #write to fasta files
            for count, line in enumerate(f, start=0):
                if count % 4 == 0:
                    lineA = line.decode()
                elif count % 4 == 1:
                    lineB = line.decode()
                elif count % 4 == 2:
                    lineC = line.decode()
                elif count % 4 == 3:
                    lineD = line.decode()
                    #if len(lineB) == 37: #filter by 36 nt length (plus newline character)
                    if len(lineB) == 41:  # filter by 36 nt length (plus newline character)
                        if (lineB[12:15] == 'CGA' and lineB[21:24] == 'TGC') or (lineB[12:15] == 'GCA' and lineB[21:24] == 'TCG'): #filter by BCG1 cutsites
                            f2.write(lineA[:-5]+'36_0'+'\n')
                            f2.write(lineB[:-5]+'\n')
                            f2.write(lineC)
                            f2.write(lineD)
                            countCorrect += 1
                        elif (lineB[12:15] == 'CGA' and lineB[21:24] == 'TCG') or (lineB[12:15] == 'GCA' and lineB[21:24] == 'TGC'): #filter by mismatched cutsites
                            countBCGmiss += 1
                        else:
                            countWrongSite += 1
                    else:
                        countWrongLength += 1

    return countCorrect, countWrongLength, countBCGmiss, countWrongSite #return counts

def main():

    #directory = "D:/Hawaii_2022/20230802_2bRADseq_fixed/FastP_Out/fastqgz" #file directory
    directory = "D:/Florida_2023/THIS_Florida_FastP_Merged"  # file directory

    for root, dirs, files in os.walk(directory): #walk through file tree
        for name in files:
            if "_M_" in name and "fastq.gz" in name: #make sure merged and fastq.gz filetype
                filename = os.path.join(root, name)
                correct, wrongLength, BCGmiss, wrongSite = load(filename) #run function
                print(name, correct, wrongLength, BCGmiss, wrongSite) #print counts

main()