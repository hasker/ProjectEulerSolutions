#!/usr/bin/python

n = 100

rangeSum = n*(n+1)/2
squareSum = 0

for i in range (1, n+1):
	squareSum += i * i

print rangeSum ** 2 - squareSum
