from sys import argv

script, s, t = argv

n = len(s)
mismatch = 0
i = 0

while n > 0:
	if s[i] is t[i]:
		n = n - 1
		i = i + 1
	else:
		mismatch = mismatch + 1
		n = n - 1
		i = i + 1


print mismatch