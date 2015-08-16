from sys import argv

script, months, months_alive = argv

n = int(months)
m = int(months_alive)

total_list = []
total = 0
i = 0 #this is an index, when i = 1 this is F(2)
j = 1
x = 1 ##x keeps track of the month
while x <= n:
	if x == 1: #month 1 is baby rabbits to start
		total_list.append(1)
	elif x == 2: #month 2 is mature rabbits
		total_list.append(1)
	elif x > 2 and x <= m: #the rabbits start to mate
		total = total_list[i] + total_list[j] 
		total_list.append(total)
		i = i + 1 
		j = j + 1
	elif x > m: #x is greater than the lifespan of rabbits, one pair will be gone each month
		##needed a little help on this part. understood completely now. Equation changes 
		##once rabbits start dying. 
		rabbits = 0
		for t in range(x-m, x-1):
			rabbits = rabbits + total_list[t-1]
		total_list.append(rabbits)
		i = i + 1
		j = j + 1
	x = x + 1


print total_list[-1]