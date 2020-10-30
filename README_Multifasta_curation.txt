Soler-Camargo et al, 2020. The role of in silico predicted pseudogenes in the genomic plasticity of the Mycobacterium tuberculosis complex


INPUT files:

1 - The cds fna and cds faa files of each strain downloaded from NCBI.
2 - The pseudoene DNA dataset files generated with Pseud_retriev.py algorithm of each genome.

Put the files in a directory with the Multifasta_curation.py algorithm and run the following comand:

python3 Multifasta_curation.py


OUTPUT files:

1 - The "xxx_genomic_nt_CURATED.fasta" file, that contains the nucleotide sequences of all genes and true pseudogenes predicted by PGAP of NCBI.
2 - The "xxx_genomic_aa_CURATED.fasta" file, that contains the amino acid sequences of all genes and true pseudogenes predicted by PGAP of NCBI.


NOTES:

- The cds fna and cds faa must have the exactly names before the "_cds_from_genomic.fna" and "_translated_cds.faa" identification.

- We recomend do not change the name of the files downloaded from NCBI.

- Do not put any other .fna and .faa file in the directory.

- You may run this algorithm for all analyzed genomes at once.

