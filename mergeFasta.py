"""
Takes in text file of reads from both lanes and returns fasta file
8-14-23
Richard Grewelle
"""

import os #to walk through file tree


def main():
    directory = "D:/20230802_2bRADseq_fixed/FastP_Out"  # file directory
    files = []

    for root, dirs, filer in os.walk(directory):  # walk through file tree
        for name in filer:
            if '.gz' not in name and 'joined' not in name: #exclude other files in folder
                files.append(name) #add to list of files to join
    for i in range(1,len(files)):
        if i%2 != 0 and files[i][0:5] == files[i-1][0:5]: # merge lanes 1 and 2
            filename = directory + '/' + files[i][:-21] + '_joined.fa'
            with open(filename, 'w') as outfile:
                for fname in [files[i-1], files[i]]:
                    numLine = 0
                    with open(directory + '/' + fname) as infile:
                        for line in infile:
                            numLine += 1
                            outfile.write('>' + 'read_' + str(numLine) + '\n')  # add fasta format
                            outfile.write(line)

main()