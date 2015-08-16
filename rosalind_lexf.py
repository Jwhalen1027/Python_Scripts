from sys import argv
import itertools

script, string, length = argv

length = int(length)
list = itertools.product(string, repeat = length) 
for element in list:
	print ''.join(element)
	

