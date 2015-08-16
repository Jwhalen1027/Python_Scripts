from sys import argv 

script, a, b, c, d, e, f = argv
a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)




domdom = 2.0*a
domhet = 2.0*b
domrec = 2.0*c
hethet = 2.0*d*0.75
hetrec = 2*(.5)*e
recrec = 0

dominants = domdom+domhet+domrec+hethet+hetrec+recrec

print dominants