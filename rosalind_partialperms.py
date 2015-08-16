import sys
import math

n = int(sys.argv[1])
k = int(sys.argv[2])
#this is the equation for the number of permutations from a list length n with permutation length k
diff = (n - k)
answer = ((math.factorial(n))/(math.factorial(diff)))%1000000
print answer