#!/usr/bin/env python3

import glob
from Bio import SeqIO


#getting the primer sequence

pf = input('Insert the nucleotide sequence of the forward primer: ' )
pr = input('Insert the nucleotide sequence of the reverse primer: ')

pf = pf.upper()
pr = pr.upper()

#output
out = open('PCR_product_sizes.txt', 'w')

#searching primers among genomes

for file in glob.glob('*.fna'):

	flag = 0
	for seq_record in SeqIO.parse(file, "fasta"):

		sequence = seq_record.seq

		if pf in sequence and pr in sequence:
		
			forward = sequence.find(pf)
			reverse = sequence.find(pr)
			tam_rev = len(pr)
			bp = tam_rev + reverse - forward

			line = 'PCR product size (bp): ' + '\t' + str(bp) + '\t' + file + '\n'
			out.writelines(line)
			flag = 1
	if flag == 0:

		line = 'PCR product not found due to a primer missidentification' + '\t' + file + '\n'
		out.writelines(line)
 


out.close()



	


	

	

