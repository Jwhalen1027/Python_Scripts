from sys import argv
import itertools

script, n = argv

n = int(n)
perm_length = n  
perm_list = []
##Make lists of lists with the signed values
##ie [(-1,1), (-2,2), (-3,3)]
for i in range(1,n+1):
	perm_list.append([-i, i])
#print perm_list
	
perm_products = map(list,(list(itertools.product(*perm_list)))) ##'*args' is an unknown number of arguments
##in this case, n (or len(perm_list)). Product (perm_list1, perm_list2...perm_listn). 
##First position in 1 matches with all postions in 2-n and so on. Map function turns every product into a list
#print perm_products


all_permutations = []
for perm in perm_products:
	all_permutations += (map(list, list(itertools.permutations(perm))))
print len(all_permutations)


for element in all_permutations:
	element = str(element)
	element = element.replace('[', '')
	element = element.replace(']', '')
	element = element.replace(',', '')
	print element
	