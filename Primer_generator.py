#!/usr/bin/env python3

import glob
from Bio import SeqIO


out = open('nr_primer_database.txt', 'w')

nr_primer = {}
primer_list = []

for file in glob.glob('*.faa'):

	for seq_record in SeqIO.parse(file, "fasta"):

		sequence = seq_record.seq

		primer = str(sequence[:15])

		if primer in nr_primer:
			nr_primer[primer] +=1

		else:
			nr_primer[primer] = 1


for primer in nr_primer:

	line = primer + '\n'
	out.writelines(line)

out.close()


