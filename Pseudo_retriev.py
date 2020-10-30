#!/usr/bin/env python3

from Bio import SeqIO
import glob

print('running...')

for file in glob.glob('*.gbff'):

	count = 0
	
	genome = file
	genome = genome.replace('.gbff', '.fasta')
	out = open(genome, 'w')

	# searching in contigs
	reading = open(file, 'r')
	reading2 = reading.read()
	contigs = reading2.split('CONTIG      ')

	a = 0
	for item in contigs:

		if '/pseudo' in item:

			# seraching pseudogenes in the contig
			num = item.count('/pseudo')
			listn = item.split('/pseudo')
			
			j = 0			
			for i in listn:
				

				if j%2 != 0:

					listn2 = i.split('/locus_tag')

					if 'too short' not in listn2[1]:

						count+=1

						parts = listn2[0]
						parts = parts.split('CDS             ')
						parts = parts[1].split('\n')

						coordinates = parts[0] 

						part = parts[0].split('..')
						start = part[0]
						end = part[1]
						pos_s = ''
						pos_e = ''

						for number in start:
							if number.isdigit():
								pos_s = pos_s + number

						for number in end:
							if number.isdigit():
								pos_e = pos_e + number

						pos_s1 = int(pos_s)
						pos_e1 = int(pos_e)
						

						# seraching the pseudogene pos_stion in the fna genomic file
						fna = file
						fna = fna.replace('.gbff','.fna')

						b = 0
						for seq_record in SeqIO.parse(fna, "fasta"):


							if a == b:
								sequence = seq_record.seq
								pos_s2 = pos_s1-1


								headline = '>' + coordinates + '\t' + seq_record.id + seq_record.description + '\n'
								line = sequence[pos_s2:pos_e1] + '\n'
								out.writelines(headline)
								out.writelines(line)
							b+=1

				j+=1

		a+=1
	print(file, count)
	out.close()



