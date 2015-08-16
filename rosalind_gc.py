#f = open('/Users/JWhalen/Downloads/rosalind_gc.txt')

from __future__ import division

g_count = 0
c_count = 0
gc_count = 0
total_count = 0.0
content = 0.0
high_content = 1.0
high_line = ''
total_gc_count = 0
#line = f.readline()
content_line = ''

with open('/Users/JWhalen/Downloads/rosalind_gc-5.txt') as f:
	for line in f:
		if line.startswith('>'):
			if total_count > 0:
				content = (total_gc_count / (total_count)) * 100.0 
			#content_line = line[1:]
			total_gc_count = 0
			total_count = 0
			if content > high_content:
				high_line = content_line
				high_content = content
			content = 0
			content_line = line[1:]
		else:
			for nucleotide in line:
				if nucleotide is ('C'):
					c_count = c_count + 1
					total_count = total_count + 1
				elif nucleotide is ('G'):
					g_count = g_count + 1
					total_count = total_count + 1
				elif nucleotide is ('A'):
					total_count = total_count + 1
				elif nucleotide is ('T'):
					total_count = total_count + 1
			gc_count = c_count + g_count
			total_gc_count = total_gc_count + gc_count
			c_count = 0
			g_count = 0
			gc_count = 0

content = (total_gc_count / total_count) * 100
if content > high_content:
				high_content = content
				high_line = content_line


			
			
	
	

print high_line, high_content



f.close

	
