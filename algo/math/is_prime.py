import math as m

"""
	Return true or false, indicating whether a given number n is a prime
"""
def solution(n):
	if n < 2:
		return False;
	maxDivisor = m.ceil(m.sqrt(n))
	for i in range(2, maxDivisor+1):
		if n % i ==0 & n != i: 
			return False
	return True