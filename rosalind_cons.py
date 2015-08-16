import numpy

f = open('/Users/jeannewhalen/Downloads/rosalind_cons-9.txt', 'r')

seq_list = []
dna = ''
for line in f:
	if line.startswith('>'):
		seq_list.append(dna)
		dna = ''
	else:
		line = str(line)
		line = line.strip('\n')
		dna = dna + line
seq_list.append(dna)
##This gives a list of sequences
seq_list.pop(0)



seq_lengths = len(seq_list[0])
consensus = numpy.zeros((4,seq_lengths), dtype=numpy.int)
##generates a matrix with zeroes. Row 1 is A, 2 is C, 3 is G, 4 is T
#seq_test = seq_list[0]
#print seq_test[0]

for seq in seq_list:
	i = 0
	for char in seq:
		if char is 'A':
			consensus[(0, i)] += 1
		elif char == 'C':
			consensus[(1, i)] += 1
		elif char == 'G':
			consensus[(2, i)] += 1
		elif char == 'T':
			consensus[(3, i)] += 1
		i = i + 1
##Generates the consensus matrix


#print seq_lengths
j = 0
location_indices = []
while j < seq_lengths:
	location = consensus[:,j]
	location_indices.append(numpy.argmax(location))
	j = j + 1
#location_indices.append(numpy.argmax(location))
#print len(location_indices)

consensus_string = ''	
for locate in location_indices:
	if locate == 0:
		consensus_string += 'A'
	elif locate == 1:
		consensus_string += 'C'
	elif locate == 2:
		consensus_string += 'G'
	elif locate == 3:
		consensus_string += 'T'
print consensus_string

a_mat = numpy.array_str(consensus[0], max_line_width = 2*seq_lengths)
a_mat = str(a_mat)
A_string =  'A:' + a_mat
A_string = A_string.replace("["," ")
A_string = A_string.replace("]","")
print A_string		
c_mat = numpy.array_str(consensus[1], max_line_width = 2*seq_lengths)
c_mat = str(c_mat)
C_string =  'C:' + c_mat
C_string = C_string.replace("["," ")
C_string = C_string.replace("]","")
print C_string		
g_mat = numpy.array_str(consensus[2], max_line_width = 2*seq_lengths)
g_mat = str(g_mat)
G_string =  'G:' + g_mat
G_string = G_string.replace("["," ")
G_string = G_string.replace("]","")
print G_string		
t_mat = numpy.array_str(consensus[3], max_line_width = 2*seq_lengths)
t_mat = str(t_mat)
T_string =  'T:' + t_mat
T_string = T_string.replace("["," ")
T_string = T_string.replace("]","")
print T_string		
##Next is put it in the right format
##NOW THIS IS THE PART THAT IS WRONG
# t = 0
# for row in consensus:
# 	row = str(row)
# 	row = row.strip('[ ')
# 	row = row.strip(']')
# 	if t == 0:
# 		print 'A:',row
# 	elif t == 1:
# 		print 'C:',row
# 	elif t == 2:
# 		print 'G:',row
# 	elif t == 3:
# 		print 'T:',row
# 	t = t + 1
# 
	
	
	
			
			