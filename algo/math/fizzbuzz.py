def solution(n):
	"""	Given a number N, console logs the numbers from 1 to N.
	But for multiples of 3 print 'fizz' instead of the number,
	for multiples of 5, print 'buzz',
	for numbers which are multiples of both 3 and 5, print 'fizzbuzz'
	For example: 
	fizzbuzz(5);
	1
	2
	fizz
	4
	buzz"""
	for i in range(1, n+1):
		if i % 15 == 0:
			print('fizzbuzz')
		elif i % 3 == 0:
			print('fizz')
		elif i % 5 == 0:
			print('buzz')
		else:
			print(i)