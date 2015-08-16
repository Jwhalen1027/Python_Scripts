from sys import argv

script, sequence, sub = argv


i = 0
index = []


for amino_acid in sub: #for each amino acid we want to find the first occurence, but in the correct order, so don't restart the index
	while amino_acid != sequence[i]:
		i = i + 1
	else: 
		index.append(i+1)
		i = i + 1
		
print index

	
		