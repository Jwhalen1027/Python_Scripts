###Jeanne Whalen####
###Find the longest motif/substring in a FASTA file###

f = open('/Users/JWhalen/Downloads/rosalind_lcsm.txt', 'r')

seq_list = [] ##All sequences
length = [] ##Store the lengths to only find motifs shorter than the shortest sequence
the_seq = ''
seq_length = 0
for line in f:
	if line.startswith('>'): #this is a sequence title
		length.append(seq_length)
		seq_list.append(the_seq)
		the_seq = ''
	else: ##this is a sequence
		line = line.strip('\n')
		the_seq = the_seq + line
		seq_length = seq_length + len(line)
length.append(len(the_seq))
seq_list.append(the_seq)		
seq_list.pop(0)
length.pop(0)
n = min(length)
#print n


###Function Length Check will return the maximum length of all the motifs in the motif list.
###This will be used to only look at motifs of a certain size. 
def length_check(motif_list):
	length_list = []
	for motif in motif_list:
		length = len(motif)
		length_list.append(length)
	return max(length_list)

##Get Motifs will return all the unique motifs in a sequence using only the maximum possible
##length of motifs
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
motif_length = length_check(original_motif_list)


##Loop through each sequence and find motifs while updating the list of all possible motifs (unique only)
for seq in seq_list:
	seq_motif = get_motifs(seq, motif_length)	
	original_motif_list.intersection_update(seq_motif)
	motif_length = length_check(original_motif_list)

#print motif_length
##Only return the longest motifs, return those
longest_motifs = []
for mot in original_motif_list:
	mot_length = len(mot)
	if mot_length == motif_length:
		longest_motifs.append(mot)
print longest_motifs
		
	



	