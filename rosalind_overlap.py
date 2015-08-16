

fasta_list = {}
fasta2 = {}
fasta = ''
with open('/Users/JWhalen/Downloads/untitleddocument.txt', 'r') as f:
	for line in f:
		if line.startswith('>'): #this is a header, we need to save this 
			fasta = line[1:]
			fasta = fasta.rstrip()
			fasta = fasta.rstrip('\\')
			print fasta
			fasta_list[fasta] = 1
			fasta2[fasta] = 1
		else: #This is a sequence
			line = line.rstrip()
			line = line.rstrip('\\')
			fasta_list[fasta] = line[0:3]
			fasta2[fasta] = line[-3:]

#i have a dictionary with the fasta name (key) and the O3 as the value
#also have a list with the last 3 nucleotides of each fasta

#for keys, values in fasta_list.items():
#	print keys, values

#for keys, values in fasta2.items():
#	print keys, values


# for value in fasta_list.values():
# 	print value
# 	if value in list2:
# 		
# 		print fasta_list.keys(), fasta2.keys()
# 

