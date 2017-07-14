#!/usr/bin/env python
#Align barcode amplicon reads to s288c reference genome

import sys
import os

def main():
    forward = sys.argv[1]

    print("Downloading current release of s288c reference genome")
#    os.system("curl http://downloads.yeastgenome.org/sequence/S288C_reference/genome_releases/S288C_reference_genome_Current_Release.tgz")
#    os.system("tar zxvf S288C_reference_genome_Current_Release.tar")
    os.chdir("S288C_reference_genome_R64-2-1_20150113")
    os.system("cp S288C_reference_sequence_R64-2-1_20150113.fsa ..")
    os.chdir("..")

    #Build s288c reference genome index
    os.system("bwa index -p s288c -a bwtsw S288C_reference_sequence_R64-2-1_20150113.fsa")

    #Map the fastq reads to s288c genome
    os.system("bwa mem -M s288c " + forward + " > tem.sam")

    print("The total number of reads is .......")
    os.system("cat " + forward + " | echo $((`wc -l`/4))")

    print ("Mapped reads number is .......")
    os.system("awk '{if ($3 !~ /\*/) print}' tem.sam | awk '{if ($2 <= 16) print}' | grep -v \^\@ | wc -l")
    os.system("rm S288C_reference_sequence_R64-2-1_20150113.fsa")
    os.system("rm s288c*")
    os.system("rm tem.sam")

if __name__ == "__main__":
    main()