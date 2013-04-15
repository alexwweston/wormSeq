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
    

    run_gmap(proj_name, final_assembly, raw_reads)

	

#
# Example:
# gmap_build -d ramanei_draft -D assembly_data/output/ramanei_draft assembly_data/output/final.assembly.fasta
# gsnap -t 32 -B 5 -n 1 -D assembly_data/output/ramanei_draft/ -d ramanei_draft -A sam lane7_NoIndex_L007_R1_009.fastq >gsnap_out.sam

def run_gmap(proj_name, final_assembly, raw_reads):


    #build index
    cmmd = "gmap_build " + "-D " + proj_name + "/gmap_out" + " -d " + proj_name + "_gmap_indices " + final_assembly
    subprocess.call(cmmd, shell=True)

    #create .sam file

    
    cmmd ="gsnap -t 32 -B 5 -n 1 " + "-D " + proj_name + "/gmap_out"  + " -d " + proj_name + "_gmap_indices "
    cmmd = cmmd + "-A sam " + raw_reads + " >" + proj_name + "/" + proj_name + ".sam"
    subprocess.call(cmmd, shell=True)
    
    
    #convert to .bam for IGV
    cmmd = "samtools view -bS " + proj_name + "/" + proj_name + ".sam>" + proj_name + "/" + proj_name + ".bam"
    subprocess.call(cmmd, shell=True)
    


if __name__ == "__main__":
    main()

