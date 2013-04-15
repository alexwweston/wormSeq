import sys
import subprocess
	

#
# Example:
# gmap_build -d ramanei_draft -D assembly_data/output/ramanei_draft assembly_data/output/final.assembly.fasta
# gsnap -t 32 -B 5 -n 1 -D assembly_data/output/ramanei_draft/ -d ramanei_draft -A sam lane7_NoIndex_L007_R1_009.fastq >gsnap_out.sam
#final_assembly and data_dir defined in automate or config reader
def run( pubgenome):
    published_genome = pubgenome[0]
    cmmd = "nucmer --prefix=" + os.path.join(data_dir, proj_name) + " " + published_genome + " " + final_assembly
    subprocess.call(cmmd, shell=True)
    
    cmmd = "delta-filter -q " + os.path.join(data_dir, proj_name) + ".delta >" + os.path.join(data_dir, proj_name) + ".filter"
    subprocess.call(cmmd, shell=True)

    cmmd = "show-tiling " + os.path.join(data_dir,proj_name) + ".filter >" + os.path.join(data_dir, proj_name) + ".tiling"
    subprocess.call(cmmd, shell=True)



