from sys import argv

script, n, k = argv

n = int(n)
k = int(k)

total_list = []
total = 0
i = 0 #this is an index, when i = 1 this is F(2)
j = 1
x = 1
while x <= n:
	if x == 1:
		total_list.append(1)
	elif x == 2:
		total_list.append(1)
	elif x > 2:
		total = (total_list[i]*k) + total_list[j] 
		total_list.append(total)
		i = i + 1 
		j = j + 1
	x = x + 1


print total_list[-1]
		