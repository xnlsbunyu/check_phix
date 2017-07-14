# check_phix
Use bwa to map the reads to phix174 reference genome

unmapped reads in sam file has * in the 3rd column

Count the number of * to get the number of reads that are not mapped to phix

fastq need to be gunzipped

usage: python check_phix.py sample.fastq


#Check s288c reads
Use bwa to map the reads to s288c reference genome

Awk to filter out uniquely mapped and count the number

usage: python check_s288c.py sample.fastq
