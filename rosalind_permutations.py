import sys
import itertools

perm_length = int(sys.argv[1])
perms = perm_length

num_list = []
while perm_length > 0:
	num_list.append(perm_length)
	perm_length = perm_length - 1
f = open('/Users/JWhalen/Desktop/permutations.txt', 'w')
#print num_list	
perm_list = list(itertools.permutations(num_list, perms))
howmany = str(len(perm_list))
f.write(howmany + '\n')

for sub_list in perm_list:
	list_string = str(sub_list)
	list_string = list_string.replace('(', '')
	list_string = list_string.replace(')', '')
	list_string = list_string.replace(',', '')
	f.write(list_string + '\n')
f.close()