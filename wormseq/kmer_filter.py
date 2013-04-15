import subprocess
from wormseq.config_reader import *

def run(conf_list):
    print "\n\t(automate) >> starting kmer_filter\n"
    subprocess.call(conf_list)
    print "\n\t(automate) >> finished kmer_filter\n"
