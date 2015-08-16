from sys import argv

script, my_string = argv

str = my_string.split() 
d = {}
for word in str:
	if word in d:
		d[word] = d[word] + 1
	else:
		d[word] = 1

for key, value in d.items():
	print key, value
	
