#!/usr/bin/python
sum = 0

for i in xrange(0,1000):
	if not i % 3:
		sum = sum + i
	elif not i % 5:
		sum = sum + i

print(sum)
