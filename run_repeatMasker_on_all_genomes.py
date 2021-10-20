import sys
import os
import multiprocessing
import subprocess
from pathlib import Path
import time

# def run_repeatMasker_MP(rm_jobs):
#     try:
OUT_DIR = '/home/ahollar/project_conserved_rnas/repeat_masker_outlogs'
GENOMES_DIR = '/home/ahollar/project_conserved_rnas/genomes'
REPEAT_MASKER_EXC = '/home/ahollar/software/RepeatMasker/RepeatMasker'

if not os.path.isdir(OUT_DIR):
    os.makedirs(OUT_DIR)

def run_repeatMasker(genome_path):
    output_log_path = os.path.join(OUT_DIR, str(str(genome_path).split('/')[-1] + ".out"))
    repeat_masker_command = ".{} --species mammals {}".format(REPEAT_MASKER_EXC, genome_path)

    print(output_log_path)
    print(repeat_masker_command)

    start_time = time.time()
    #repeat_masker_process = subprocess.Popen(repeat_masker_command, shell=True, stdout=output_log_path, stderr=subprocess.PIPE)
    #rm_stderr = repeat_masker_process.communicate()[1]
    repeat_masker_process = subprocess.run([str('.' + REPEAT_MASKER_EXC), '--species', 'mammals', genome_path], stdout=output_log_path, universal_newlines=True)
    
    print("RepeatMasker completed on {} genome in {} seconds.\n".format(genome_path, str(time.time() - start_time)))
    return repeat_masker_process

def main():
    genome_path_list = Path(GENOMES_DIR).glob('**/*.fna')

    # for genome in genome_path_list:
    #     print(genome)
    #print(genome_path_list)

    job_pool = multiprocessing.Pool()
    for repeat_masker_result in job_pool.imap_unordered(run_repeatMasker, genome_path_list):
        print(repeat_masker_result)

if __name__=='__main__':
    main()