#!/usr/bin/python

import os, sys
from wormseq import process_shortreads, kmer_filter, allpaths
from wormseq.config_reader import *

### These should be replaced by the config file inputs
barcode_filename = os.path.join(data_dir, 'ps_barcode/lane7_barcodes')
barcode_pairings = os.path.join(data_dir, 'ps_barcode/lane7_samples')

config_dictionary = read_config("automate.conf")

if 'process_shortreads' in config_dictionary.keys():
    process_shortreads.run(config_dictionary['process_shortreads'])
                           
if 'kmer_filter' in config_dictionary.keys():
    kmer_filter.run(config_dictionary['kmer_filter'])

if 'allpaths' in config_dictionary.keys():
    allpaths.run(config_dictionary['allpaths'])

if 'gmap_gsnap' in config_dictionary.keys():
    gmap_gsnap.run(config_dictionary['gmap_gsnap'])
if 'blat' in config_dictionary.keys():
    blat.run(config_dictionary['blat'])

# Parent directory for all data files
# g_dataDir = "/home3/everson/data"
# Location of necessary binary files to run pipeline
# g_binDir = "/home3/everson/cis554_scripts/bin"

# Input/output dirs for process shortreads
# ps_in_dir = os.path.join(g_dataDir, "smallData")
# ps_out_dir = os.path.join(g_dataDir, "smallOut")

# Locations of specific files relative to main data dir
# ps_barcode_file = os.path.join(g_dataDir, "lane7_barcodes")
# ps_barcode_pairing_file = os.path.join(g_dataDir, "lane7_samples")

# index of process name returns list, the first element of which is the
# executable name, and the following elements are command line args.
# This is the format for passing to the python subprocess module
# g_binaries = {
#     'process_shortreads':
#         ['/home3/everson/local/bin/process_shortreads',
#          '-P',
#          '-p', ps_in_dir,
#          # '-1', os.path.join(g_dataDir, "testData/test_1"),
#          # '-2', os.path.join(g_dataDir, "testData/test_2"),
#          '-b', ps_barcode_file,
#          '-o', ps_out_dir,
#          '-i', 'fastq',
#          '-y', 'fastq',
#          '-c',
#          # '-r',
#          '-E', 'phred33'],
#     'kmer_filter':
#         [],
# }

# if __name__ == "__main__":

#     # Grab the location of the configuration file from the command line
#     if( len(sys.argv) < 2 ):
#         print "Usage:"
#         print "    automate.py <config-file>"
#         exit(1)
#     else:
#         parseConfig()
#     shortreads_io()
