#!/bin/sh

#  gmap_gsnap_blat_mummer_run.sh
#  
#  Script for running gmap_gsnap, blat, and MUMmer
#

#Command line args:
#   $1 is the project name (user defined)
#   $2 is the final assembly, i.e. output from Allpaths
#   $3 is the published genome for C. Remanei 
#   $4 is a fastq file containing raw reads--I believe this is the
#   same as the input for AllPaths

## Run gmap-gsnap
echo $1
echo $2
echo $3
echo $4

module load gmap-gsnap
module load samtools
echo running gmapgsnap
python gmapgsnap.py $1 $2 $3 $4

module unload gmap-gsnap
module unload samtools

## Run blat
module load blat
echo running BLAT
python BLAT.py $1 $2 $3 $4

module unload blat

## Run MUMmer
module load MUMmer/3.23

echo running MUMmer
python MUMmer.py  $1 $2 $3 $4

module unload MUMmer/3.23
