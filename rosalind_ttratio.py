from sys import argv
script, dna1, dna2 = argv

i = 0
transition = 0.0
transversion = 0.0
length = len(dna1)

while i < length:
	if dna1[i] == dna2[i]:
		i = i + 1
	else:
		if (dna1[i] == 'A') and (dna2[i] == 'G'):
			transition = transition + 1.0
		elif (dna1[i] == 'G') and (dna2[i] == 'A'):
			transition = transition + 1.0
		elif (dna1[i] == 'C') and (dna2[i] == 'T'):
			transition = transition + 1.0
		elif (dna1[i] == 'T') and (dna2[i] == 'C'):
			transition = transition + 1.0
		elif (dna1[i] == 'A') or (dna1[i] == 'G') and (dna2[i] == 'C') or (dna2[i] == 'T'):
			transversion = transversion + 1.0
		elif (dna1[i] == 'C') or (dna1[i] == 'T') and (dna2[i] == 'A') or (dna2[i] == 'G'):
			transversion = transversion + 1.0
		i = i + 1

#print transition
#print transversion
ratio = (transition/transversion)

print ratio