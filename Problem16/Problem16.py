#!/usr/bin/Python3

strNum = str(2 ** 1000)

sum = 0
for i in range(0, len(strNum)):
	sum += int(strNum[i])

print sum
