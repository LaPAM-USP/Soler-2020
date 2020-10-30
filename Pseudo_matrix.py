#!/usr/bin/env python3

import numpy as np
import glob
from Bio import SeqIO
import seaborn as sns; sns.set()
from numpy import array

out = open('primer_matrix.txt', 'w') #change the name of the file when necessary
genomes = open('genomes_phylo.txt', 'r') #change the name of the file when necessary
primers = open('nr_primer_database.txt', 'r') #change the name of the file when necessary

genomes = genomes.read()
genomes = genomes.split('\n')
del genomes[-1]

primers = primers.read()
primers = primers.split('\n')
del primers[-1]

line = ''
n = 0

for item in genomes:

	out.writelines(item)
	p = 0

	while p < 1167: # change the 1167 for the number of primers when necessary

		flag = 0

		for seq_record in SeqIO.parse(item, "fasta"):

			if flag == 0:
		
				seq = str(seq_record.seq)

				if primers[p] in seq[:15]: # primer found in at least one genome

					line = '\t' + '1'
					out.writelines(line)
					flag = 1


		if flag == 0: # when primers is not found

			line = '\t' + '0'
			out.writelines(line)

		p+=1

	n+=1
	print(n, 'of 201')
	out.writelines('\n')


out.close()

