introns = []
linecount = 0
with open('/Users/JWhalen/Downloads/rosalind_splc-2.txt', 'r') as f:
	for line in f:
		linecount = linecount + 1
		if linecount == 2: #this is our main dna string
			dna = line
		elif linecount != 2 and linecount%2 == 0: #this is an intron
			intron = line 
			introns.append(intron)
print dna
#print introns
#all the introns are saved in a list and the dna is separate 
print dna[33:43]
for sequence in introns:
	print sequence
	sequence = sequence.strip()
	i = 0
	j = len(sequence)
	s = len(dna)
	#if sequence == dna[33:43]:
	#	print "YES"
	while j <= s:
		#print i, j
		if sequence == dna[i:j]: #if we find the intron
			#print 'found the intron!'
			dna = dna[0:i]+dna[(j)::]####figure out what j should be here
			j = s + 1
		else: #it's not the intron, so keep looking for it
			i += 1
			j += 1
print len(dna)

#now we have only the exonic regions so we need to translate
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
	
peptide = ''
t = 0
v = 3
rna = dna.replace('T', 'U')
print rna
while v <= len(rna):
	pep = rna[t:v]
	if pep in codon:
		peptide += codon[pep]
	else: 
		print peptide
	t = t + 3
	v = v + 3

		
	
			
				
		

