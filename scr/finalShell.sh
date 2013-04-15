#!/bin/bash -l
#PBS -N Assembly
#PBS -q fat

# the following lines are not required, but can be useful
# for debugging purposes:
#diplays PBS work directory
WORKING_DIRECTORY='/home11/azada/Azad/'
cd $WORKING_DIRECTORY
#the working directory is supposed to contain the shuffleSequences_fastq.pl script to shuffle outputs of the kmer_filter
#the working directory is where ./kmer_filter bi-nary file and assembly_data folder exist, assembly_data folder contains 439_1, 439_2.fastq reads.

mkdir -p jennaProject/inputData

./kmer_filter -1 assembly_data/439_1.fastq -2 assembly_data/439_1.fastq -o $WORKING_DIRECTORY/jennaProject/inputData/ -D --rare --abundant

cp assembly_data/shuffleSequences_fastq.pl jennaProject/inputData/
cd jennaProject/inputData/
perl shuffleSequences_fastq.pl 439_1.fil.fastq 439_2.fil.fastq 439_shuffled.fastq
module load allpathslg
PrepareAllPathsInputs.pl DATA_DIR=$WORKING_DIRECTORY/assembly_data/
