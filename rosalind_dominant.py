from __future__ import division
from sys import argv


script, d, het, r = argv


r = float(r)
d = float(d)
h = float(het)
pop = d + h + r
pop1 = pop - 1
r1 = r - 1
d1 = d - 1
h1 = h - 1
rpop = (r/pop) * (r1/pop1)
hpop = (h/pop) * (h1/pop1)
rhpop = ((r/pop) * (h/pop1)) + ((h/pop) * (r/pop1))



prob_r_het = 0.5 * (rhpop) #percent recessive

prob_het = .25 * (hpop) # percent recessiv

prob_r = 1 * rpop  # percent recessive

recessive = prob_r_het + prob_het + prob_r


probability = 1 - recessive 

print probability
###Take into account how many of each!