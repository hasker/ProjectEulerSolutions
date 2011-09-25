#!/usr/bin/python
""" 
        Get the factors for a number 
        (Note: Not optimised for tail recursion) 
"""  
def factor(n):  
        if n == 1: return [1]  
        i = 2  
        limit = n**0.5  
        while i <= limit:  
                if n % i == 0:  
                        ret = factor(n/i)  
                        ret.append(i)  
                        return ret  
                i += 1  
  
        return [n]  
  
if __name__ == "__main__":  
        import sys  
        for index in xrange(1,len(sys.argv)):  
                print "Factors for %s : %s" %(sys.argv[index], str(factor(int(sys.argv[index])))) 

dictFact = {}

for i in range(1, 21, 1):
	tempDict = {}
	#print factor(i)
	for j in factor(i):
		tempDict[j] = tempDict.get(j, 0) + 1
	for k in tempDict:
		if tempDict[k] > dictFact.get(k, 0):
			#print dictFact[k]
			dictFact[k] = tempDict[k]

answer = 1
for l in dictFact:
	answer *= l ** dictFact[l]

print answer
