#!/usr/bin/python

for i in range(1, 501):
	for j in range(1, 501):
		if i + j - (i*j)/1000 == 500 and (i*j) % 1000 == 0:
			print "Found One:"
			print i
			print j
			print i * j * (1000 - i - j)
