from sys import argv

script, dna = argv

codon = {'TTT' : 'F', 'TTC' : 'F', 'TTA' : 'L', 'TTG' : 'L', 
	'CTT' : 'L', 'CTC' : 'L', 'CTA' : 'L', 'CTG' : 'L', 
	'ATT' : 'I', 'ATC' : 'I', 'ATA' : 'I', 'ATG' : 'M', 
	'GTT' : 'V', 'GTC' : 'V', 'GTA' : 'V', 'GTG' : 'V', 
	'TCT' : 'S', 'TCC' : 'S', 'TCA' : 'S', 'TCG' : 'S', 
	'CCT' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 
	'ACT' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 
	'GCT' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A', 
	'TAT' : 'Y', 'TAC' : 'Y', 'CAT' : 'H', 'CAC' : 'H', 
	'CAA' : 'Q', 'CAG' : 'Q', 'AAT' : 'N', 'AAC' : 'N',
	'AAA' : 'K', 'AAG' : 'K', 'GAT' : 'D', 'GAC' : 'D', 
	'GAA' : 'E', 'GAG' : 'E', 'TGT' : 'C', 'TGC' : 'C', 
	'TGG' : 'W', 'CGT' : 'R', 'CGC' : 'R', 'CGA' : 'R', 
	'CGG' : 'R', 'GGT' : 'G', 'GGC' : 'G', 'GGA' : 'G', 
	'GGG' : 'G', 'AGA' : 'R', 'AGT' : 'S', 'AGG' : 'R', 
	'AGC' : 'S'}

##TAA, TAG, TGA are all stop codons

i = 0
j = 3
dictionary = {}
while j < len(dna):
	substring = dna[i:j]
	if substring == 'ATG': # we found a start codon
		dictionary[substring] = i
	elif substring == 'TAG' or substring == 'TAA' or substring == 'TGA':
		dictionary[substring] = i

for key, item in dictionary.items():
	print key, value
		