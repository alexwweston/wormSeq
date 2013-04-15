import sys
import subprocess


#final_assembly and proj_name should be global variables defined in 
#config reader
def run( pubgenome):
    published_genome = pubgenome[0]
    cmmd = "blat " + published_genome + " " + final_assembly + ">" + os.path.join(datadir, "BLAT/") + proj_name + ".psl"
    subprocess.call(cmmd, shell=True)




