from sys import argv

script, mrna = argv

codon = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L', 
	'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', 
	'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M', 
	'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V', 
	'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', 
	'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 
	'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 
	'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A', 
	'UAU' : 'Y', 'UAC' : 'Y', 'CAU' : 'H', 'CAC' : 'H', 
	'CAA' : 'Q', 'CAG' : 'Q', 'AAU' : 'N', 'AAC' : 'N',
	'AAA' : 'K', 'AAG' : 'K', 'GAU' : 'D', 'GAC' : 'D', 
	'GAA' : 'E', 'GAG' : 'E', 'UGU' : 'C', 'UGC' : 'C', 
	'UGG' : 'W', 'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 
	'CGG' : 'R', 'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 
	'GGG' : 'G', 'AGA' : 'R', 'AGU' : 'S', 'AGG' : 'R', 
	'AGC' : 'S'}
	
##UAA, UAG, UGA are all stop codons


peptide = ''
i = 0
j = 3

while j <= len(mrna):
	pep = mrna[i:j]
	if pep in codon:
		peptide += codon[pep]
	else: 
		print peptide
	j = j + 3
	i = i + 3



	
	