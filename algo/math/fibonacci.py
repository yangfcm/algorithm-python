def solution1(n):
	if n < 2:
		return n
	return solution1(n-1) + solution1(n-2)

def solution2(n, ac1=1, ac2=1):
	if n <= 2:
		return ac2
	return solution2(n-1, ac2, ac1+ac2)

def solution3(n):
	fiboList = [0, 1]
	for i in range(2, n+1):
		a = fiboList[i-1]
		b = fiboList[i-2]
		fiboList.append(a+b)
	return fiboList[n]