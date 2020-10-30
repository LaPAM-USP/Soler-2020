#!/usr/bin/env python3

import glob
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

for file in glob.glob('*.fna'):

	print('running...')

	nt_dataset = file.replace('_cds_from_genomic.fna', '_genomic.fasta') #Pseudogene DNA dataset
	aa = file.replace('_cds_from_genomic.fna', '_translated_cds.faa')

	#OUTPUT

	out = file.replace('_genomic.fna', '_genomic_nt_CURATED.fasta')
	out_nt = open(out, 'w')

	out = file.replace('_genomic.fna', '_genomic_aa_CURATED.fasta')
	out_aa = open(out, 'w')

	# copying the protein sequences

	for seq_record in SeqIO.parse(file, "fasta"):

		if 'pseudo=true' not in seq_record.description:

			line = '>' + seq_record.description + '\n' + seq_record.seq + '\n'
			out_nt.writelines(line)


	for seq_record in SeqIO.parse(aa, "fasta"):

		if 'pseudo=true' not in seq_record.description:

			line = '>' + seq_record.description + '\n' + seq_record.seq + '\n'
			out_aa.writelines(line)
			

	# identification of true pseudogenes among cds sequences


	pseudo_id_list = []
	p = 0

	for seq_rec in SeqIO.parse(nt_dataset, "fasta"):

		flag = 0

		extracted = seq_rec.seq
		my_dna = Seq(str(extracted), generic_dna)
		extracted_rc = my_dna.reverse_complement()


		for seq_reco in SeqIO.parse(file, "fasta"):

			if 'pseudo=true' in seq_reco.description:

				cds = seq_reco.seq

				# comparing forward sequences

				if extracted == cds:

					if flag == 0:
				
						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted[1:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted[2:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted[3:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				# comparing reverse sequences

				elif extracted_rc == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted_rc[1:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted_rc[2:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1

				elif extracted_rc[3:] == cds:

					if flag == 0:

						line = '>' + seq_reco.description + '\n' + seq_reco.seq + '\n'
						out_nt.writelines(line)
						flag = 1

						pseudo_id_list.append('')
						pseudo_id_list[p] = seq_reco.description
						p+=1


	for seq_record in SeqIO.parse(aa, "fasta"):

		if 'pseudo=true' in seq_record.description:

			desc = seq_record.description
			desc = desc.replace('_prot_', '_cds_')
			
			if desc in pseudo_id_list:

				line = '>' + desc + '\n' + seq_record.seq + '\n'
				out_aa.writelines(line)

out_nt.close()
out_aa.close()
				

