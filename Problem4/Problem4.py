#!/usr/bin/python
#This makes the assumption that we find a six digit palindrome!  Not very good.

import sys

def palTest(testNum):
	strNum = str(testNum)
	if len(strNum) == 2:
		if strNum[1] != strNum[0]:
			return False
	for i in range(len(strNum)-1, len(strNum)/2-1, -1):
		if strNum[i] != strNum[len(strNum) - 1 - i]:
			return False
	else:
		return True

maxSoFar = 0

for i in range(999,1, -1):
	for j in range(999,1, -1):
		if (i * j > maxSoFar) and palTest(i * j):
			maxSoFar = i * j
			print maxSoFar
