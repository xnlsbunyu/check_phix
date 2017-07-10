# check_phix
Use bwa to map the reads to phix174 reference genome
unmapped reads in sam file has * in the 3rd column
Count the number of * to get the number of reads that are not mapped to phix
fastq need to be gunzipped
usage: python check_phix.py sample.fastq
