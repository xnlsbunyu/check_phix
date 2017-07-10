#!/usr/bin/env python
# Check the phix reads in fastq file
# bwa and phix reference genome need to be installed and indexed first

import sys
import os

def main():
    forward = sys.argv[1]


    #Download the PhiX174 reference genome from NCBI
    print ("Getting PhiX sequence from NCBI......")
    os.system("curl ftp://ftp.ncbi.nlm.nih.gov/genomes/Viruses/Enterobacteria_phage_phiX174_sensu_lato_uid14015/NC_001422.fna > phix174.fasta")

    #Build phix index using bwa
    os.system("bwa index -p phix -a bwtsw phix174.fasta")
    
    #Map fastq reads to phix genome
    os.system("bwa mem -M phix " + forward +" > tem.sam")
   
    print("The total number of reads is .......")
    os.system("awk '/\@/' " + forward + " | wc -l")

    #find mapped reads in sam file
    print ("Unmapped reads number is ......")
    os.system("awk '/\*/' tem.sam | wc -l")
    os.system("rm phix174.fasta")
    os.system("rm phix*")
    os.system("rm tem.sam")


if __name__ == "__main__":
    main()
