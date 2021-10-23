import sys
import os
import multiprocessing
import subprocess
from pathlib import Path
import time

OUT_DIR = '/home/ahollar/project_conserved_rnas/repeat_masker_outlogs'
GENOMES_DIR = '/home/ahollar/project_conserved_rnas/genomes'
REPEAT_MASKER_EXC = '/home/ahollar/software/RepeatMasker/RepeatMasker'

def run_repeatMasker(genome_path):
    output_log_path = open(os.path.join(OUT_DIR, str(str(genome_path).split('/')[-1] + ".out")), 'w')
    repeat_masker_process = subprocess.run([REPEAT_MASKER_EXC, '--species', 'mammals', '--par', '23', '--q', str(genome_path)], stdout=output_log_path, universal_newlines=True)    
    output_log_path.close()
    return repeat_masker_process

def main():
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)

    genome_path_list = Path(GENOMES_DIR).glob('**/*.fna')

    for genome in genome_path_list:
        start_time = time.time()
        if os.path.exists("".join([str(genome), ".masked"])):
            print("RepeatMasker already completed on the {} genome.".format(str(genome)))
            continue
        repeat_masker_output = run_repeatMasker(str(genome))
        print("RepeatMasker completed on {} genome in {} seconds.\n".format(str(genome), str(time.time() - start_time)))

if __name__=='__main__':
    main()