from sys import argv

script, dna = argv
num_A = 0
num_C = 0
num_G = 0
num_T = 0
for nucleotide in dna:
	if nucleotide is ('A'):
		num_A = num_A + 1
	elif nucleotide is ('C'):
		num_C = num_C + 1
	elif nucleotide is ('G'):
		num_G = num_G + 1
	elif nucleotide is ('T'):
		num_T = num_T + 1

print "%d %d %d %d" % (num_A, num_C, num_G, num_T)