#!/usr/bin/env python
#Align barcode amplicon reads to s288c reference genome

import sys
import os

def main():
    forward = sys.argv[1]
#Check whether reference genome exists or not   
    if os.path.isfile("S288C_reference_genome_Current_Release.tgz"):
        print("Reference genome is available!")
    else:
        print("Downloading current release of s288c reference genome")
        os.system("curl -OL http://downloads.yeastgenome.org/sequence/S288C_reference/genome_releases/S288C_reference_genome_Current_Release.tgz > S288C_reference_genome_Current_Release.tgz")
    os.system("tar xvzf S288C_reference_genome_Current_Release.tgz")
    os.chdir("S288C_reference_genome_R64-2-1_20150113")
    os.system("cp S288C_reference_sequence_R64-2-1_20150113.fsa ..")
    os.chdir("..")

    #Build s288c reference genome index
    os.system("bwa index -p s288c -a bwtsw S288C_reference_sequence_R64-2-1_20150113.fsa")

    #Map the fastq reads to s288c genome
    os.system("bwa mem -M s288c " + forward + " > tem.sam")

    print("The total number of reads is .......")
    os.system("cat " + forward + " | echo $((`wc -l`/4))")

    os.system("awk '{if ($3 !~ /\*/) print}' tem.sam | awk '{if ($2 <= 16) print}' | grep -v \^\@ > mapped.txt")
    print ("Mapped reads number is .......")
    os.system("wc -l mapped.txt")
    #Extract the sequence ids from the mapped.txt (The first field) and add the @ at the beginning of the line
    os.system("awk '{print $1}' mapped.txt | sed 's/^/@/' > id_list.txt ")
    #grep the sequence read (all four lines) by the id list
    os.system("grep -A 3 -f id_list.txt " + forward + " | sed '/^--$/d' > yeast_reads.fastq")
    os.system("rm S288C_reference_sequence_R64-2-1_20150113.fsa")
    os.system("rm s288c*")
    os.system("rm tem.sam")

if __name__ == "__main__":
    main()
