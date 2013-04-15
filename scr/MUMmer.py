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

    run_MUMmer(proj_name, final_assembly, published_genome)

	

#
# Example:
# gmap_build -d ramanei_draft -D assembly_data/output/ramanei_draft assembly_data/output/final.assembly.fasta
# gsnap -t 32 -B 5 -n 1 -D assembly_data/output/ramanei_draft/ -d ramanei_draft -A sam lane7_NoIndex_L007_R1_009.fastq >gsnap_out.sam


def run_MUMmer(proj_name, final_assembly, published_genome):
    #load MUMmer
    cmmd = "nucmer --prefix=" + proj_name+ "/" + proj_name + " " + published_genome + " " + final_assembly
    subprocess.call(cmmd, shell=True)
    
    cmmd = "delta-filter -q " + proj_name+ "/" + proj_name + ".delta >" + proj_name+ "/" + proj_name + ".filter"
    subprocess.call(cmmd, shell=True)

    cmmd = "show-tiling " + proj_name+ "/" + proj_name + ".filter >" + proj_name+ "/" + proj_name + ".tiling"
    subprocess.call(cmmd, shell=True)

if __name__ == "__main__":
    main()

