#!/usr/bin/python

i = 1
j = 1
k = 0
sum = 0

while j <= 4000000:
	if j % 2 == 0:
		sum = sum + j
	k = j
	j = j + i
	i = k
print (sum)
