from sys import argv

script, dna = argv


revcom = dna[::-1] #there is no reverse function so you have to use slices. 
revcom = revcom.replace('A', 'Z')
revcom = revcom.replace('C', 'Y')
revcom = revcom.replace('G', 'C')
revcom = revcom.replace('T', 'A')
revcom = revcom.replace('Z', 'T')
revcom = revcom.replace('Y', 'G')


print revcom