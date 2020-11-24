import pytest 
from algo.math import is_prime

class TestIsPrime:
	NotPrimeTestData = [
		0,1,2,10000, 68, 99, 104731
	]

	IsPrimeTestData = [
		3, 17, 8179, 104729 
	]

	@pytest.mark.parametrize("num", NotPrimeTestData)
	def test_not_prime(self, num):
		assert is_prime.solution(num) == False

	@pytest.mark.parametrize("num", IsPrimeTestData)
	def test_is_prime(self,num):
		assert is_prime.solution(num) == True

	