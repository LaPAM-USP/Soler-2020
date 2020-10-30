Soler-Camargo et al, 2020. The role of in silico predicted pseudogenes in the genomic plasticity of the Mycobacterium tuberculosis complex


INPUT files:

1 - The gbff and genomic fna files of each genome downloaded from NCBI.

Put the files in a directory with the Pseudo_retriev.py algorithm and run the following comand:

python3 Pseudo_retriev.py


OUTPUT files:

1 - The "xxx.fasta" file, that contains the nucleotide sequences of all true pseudogenes predicted by PGAP of NCBI.


NOTES:

- The gbff and genomic fna files must have the exactly name.

- We recomend do not change the name of the files downloaded from NCBI.

- Do not put any other .gbff and .fna files in the directory.

- You may run this algorithm for all analyzed genomes at once.

- The algorithm accepts complete and incomplete (draft) genomes.

- The algorithm shows the number of true pseudogenes of each strain.  
