from sys import argv

script, dna, motif = argv


i = 0
j = len(motif)
locations = []
n = 0
while n < (len(dna)) :
	sub = dna[i:j]
	if sub == motif:
		locations.append(i + 1) #push i to a list
	i = i + 1
	n = n + 1
	j = j + 1
	
	
print locations


	
	
	