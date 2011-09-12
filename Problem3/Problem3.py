#!/usr/bin/python

num = 600851475143


def firstPrime(target):
	i = 2
	while target % i != 0:
		i = i + 1
	if i == target:
		print (target)
		return target
	firstPrime(target / i)
	return

firstPrime(num)
