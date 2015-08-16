###share_motif.py####
###Find the longest the shared motifs of all sequences in FASTA file###
###Jeanne Whalen

f = open('/Users/JWhalen/Desktop/Rosalind/rosalind_pper.txt', 'r') ##FASTA File

seq_list = [] ##All the fasta sequences
length = [] ##Store the lengths to only find motifs shorter than the shortest sequence
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
seq_list.pop(0) ##empty sequence to initialize
length.pop(0) ##empty sequence to initialize
n = min(length)


motifs = []
seq_motifs = []
i = 0
j = min(length) ##The longest motif can not be longer than the shortest sequence. Iterator
z = 1
the_max = min(length) ##This will decrease until the length of the motif is found 
for sequence in seq_list:
	if seq_motifs:
		seqs = set(seq_motifs) ##unique elements only
		motifs.append(seq_motifs)
		result = set(motifs[0])
		result.intersection_update(seqs) ##find the motifs that are in the current sequence AND all the previous seqs
		motifs[0] = result
		all_lengths = []
		for item in motifs[0]:
			thelength = len(item)
			all_lengths.append(thelength)
			the_max = max(all_lengths) ##this changes to only the longest POSSIBLE motifs are found
		seq_motifs = []
	i = 0 
	j = the_max
	x = the_max
	t = 0
	while x > 1: ##Determine what length all considered motifs should be 
		i = 0
		j = the_max - t
		x = x - 1
		while j <= len(sequence): #Find all the motifs for a sequence
			motif = sequence[i:j]
			seq_motifs.append(motif)				
			i = i + 1
			j = j + 1
		t = t + 1
	z = z + 1



motifs.append(seq_motifs)
result = set(motifs[0])
seqs = set(seq_motifs)
result.intersection_update(seqs) ##Intersection one more time for final sequence
for mot in result:
	print mot
