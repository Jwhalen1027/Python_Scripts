f = open('/Users/JWhalen/Downloads/rosalind_lcsm-4.txt', 'r')




seq_list = []
length = []
the_seq = ''
seq_length = 0
for line in f:
	if line.startswith('>'): #this is a sequence, not sequence title
		length.append(seq_length)
		seq_list.append(the_seq)
		the_seq = ''
	else:
		line = line.strip('\n')
		the_seq = the_seq + line
		seq_length = seq_length + len(line)
length.append(len(the_seq))
seq_list.append(the_seq)		
seq_list.pop(0)
length.pop(0)
#print seq_list
n = min(length)
#print len(seq_list)
#print n


###Function Length Check will return the maximum length of all the motifs in the motif list.
###This will be used so we only look at motifs of a certain size. 
def length_check(motif_list):
	length_list = []
	for motif in motif_list:
		length = len(motif)
		length_list.append(length)
	return max(length_list)

def get_motifs(sequence, maximum_length):
	motif_list = []
	start = 0
	finish = maximum_length
	my_max = maximum_length
	t = 0
	while my_max > 1:
		start = 0
		finish = maximum_length - t
		my_max = my_max - 1
		while finish <= len(sequence):
			motif = sequence[start:finish]
			motif_list.append(motif)
			start = start + 1
			finish = finish + 1
		t = t + 1
	return set(motif_list)
	#print motif_list


##Initialize my motif list and lengths here
original_motif_list =  get_motifs(seq_list[0], n)
#print original_motif_list
motif_length = length_check(original_motif_list)
#print motif_length
#print len(seq_list[0])

for seq in seq_list:
	seq_motif = get_motifs(seq, motif_length)	
	original_motif_list.intersection_update(seq_motif)
	#print original_motif_list
	motif_length = length_check(original_motif_list)

print motif_length
longest_motifs = []
for mot in original_motif_list:
	mot_length = len(mot)
	if mot_length == motif_length:
		longest_motifs.append(mot)
print longest_motifs
		
	







# motifs.append(seq_motifs)
# result = set(motifs[0])
# seqs = set(seq_motifs)
# result.intersection_update(seqs)
# for mot in result:
# 	print mot



	