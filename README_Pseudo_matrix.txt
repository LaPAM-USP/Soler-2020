Soler-Camargo et al, 2020. The role of in silico predicted pseudogenes in the genomic plasticity of the Mycobacterium tuberculosis complex


INPUT files:

1 - A file that contains a list of genomes that were analyzed.
2 - The file "nr_primer_database.txt" generated with the Primer_generator.py algorithm.
3 - Only the pseudogenes amino acid sequences of the cds faa CURATED file generated with Multifasta_curation.py. When running for counterpart searches, the cds faa CURATED file must contain only the protein sequences (i.e., without pseudogene amino acid sequences).

Put the files in a directory with the Multifasta_curation.py fle and run the following comand:

python3 Pseudo_matrix.py


OUTPUT files:

1 - The "primer_matrix.txt" file, that contains the 0's and 1's matrix representing the absence and presence of a pseudogene in all analyzed genomes.

NOTES:

- The name of the genomes in the list file must be the same as the cds faa CURATED files.


