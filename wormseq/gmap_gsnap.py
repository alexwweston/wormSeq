import sys
import subprocess
	

#
# Example:
# gmap_build -d ramanei_draft -D assembly_data/output/ramanei_draft assembly_data/output/final.assembly.fasta
# gsnap -t 32 -B 5 -n 1 -D assembly_data/output/ramanei_draft/ -d ramanei_draft -A sam lane7_NoIndex_L007_R1_009.fastq >gsnap_out.sam

#global variables defined in automate or config reader
def run(gmap_args):


    #build index
    cmmd = "gmap_build " + "-D " + os.path.join(data_dir,"gmap_out") + " -d " + proj_name + "_gmap_indices " + final_assembly
    subprocess.call(cmmd, shell=True)

    #create .sam file

    
    cmmd ="gsnap -t 32 -B 5 -n 1 " + "-D " + os.path.join(data_dir, "gmap_out")  + " -d " + proj_name + "_gmap_indices "
    cmmd = cmmd + "-A sam " + raw_reads + " >" + data_dir + "/" + proj_name + ".sam"
    subprocess.call(cmmd, shell=True)
    
    
    #convert to .bam for IGV
    cmmd = "samtools view -bS " + data_dir + "/" + proj_name + ".sam>" + data_dir + "/" + proj_name + ".bam"
    subprocess.call(cmmd, shell=True)
    

