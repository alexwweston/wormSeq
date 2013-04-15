import sys
import subprocess


#right now, arguments are (in order) script_name
#<proj_name> <final_assembly_file> <published_genome> <raw_reads>
def main(argv = sys.argv):
    print "in main"
    args = sys.argv #grab arguments and stick them in a list
    proj_name = args[1]
    final_assembly = args[2]
    published_genome = args[3]
    raw_reads = args[4]
    
    run_blat(proj_name, final_assembly, published_genome)

	


def run_blat(proj_name, final_assembly, published_genome):
    #load blat
    #subprocess.call('module load blat', shell=True)
    
    cmmd = "blat " + published_genome + " " + final_assembly + ">" + proj_name+ "/BLAT/" + proj_name + ".psl"
    subprocess.call(cmmd, shell=True)


if __name__ == "__main__":
    main()



