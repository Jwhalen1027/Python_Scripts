from sys import argv
from collections import Counter
script, protein = argv

alist = ['F', 'F', 'L', 'L',  'L', 'L', 'L', 'L', 
	'I', 'I', 'I', 'M', 'V', 'V', 'V', 'V', 'S', 'S', 
	'S', 'S', 'P', 'P', 'P', 'P', 'T', 'T',  'T', 'T', 
	'A', 'A', 'A', 'A', 'Y', 'Y', 'H',  'H', 'Q', 'Q', 
	'N', 'N', 'K', 'K', 'D', 'D', 'E', 'E', 'C', 'C', 
	'W', 'R', 'R', 'R', 'R', 'G', 'G', 'G', 'G', 'R', 'S', 'R','S']
#print alist.count('F')
ways = 1	
for char in protein:
 	a_count = alist.count(char)
 	#print char
 	#print a_count
 	ways = a_count * ways
ways = ways * 3
mod_ways = ways%1000000 

print mod_ways