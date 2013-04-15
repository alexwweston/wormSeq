#!/bin/sh

# load all modules needed for
# pipeline
module load allpathslg
module load gmap-gsnap
module load samtools
module load blat
module load MUMmer/3.23
module load maker

#run main python script
python automate.py


#inload all modules
module unload allpathslg
module unload gmap-gsnap
module unload samtools
module unload blat
module unload MUMmer/3.23
module unload maker
