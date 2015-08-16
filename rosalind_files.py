f = open('/Users/JWhalen/Downloads/rosalind_ini5-2.txt', 'r')

n = 0


for line in f: 
	if n % 2 == 1: #this is an even line
		print line
	n = n + 1