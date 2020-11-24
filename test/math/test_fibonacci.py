
import pytest
from algo.math import fibonacci
 
class TestFibonacci: 
	testData = [
		(1, 1),
		(2, 1),
		(3, 2),
		(4, 3),
		(5, 5),
		(20, 6765)
	]

	testBigData = [
		(39, 63245986)
	]

	@pytest.mark.parametrize("num, expected", testData)
	def test_solution1(self, num, expected):
		assert fibonacci.solution1(num) == expected
	
	
	@pytest.mark.parametrize("num, expected", testData + testBigData)
	def test_solution2(self, num, expected):
		assert fibonacci.solution2(num) == expected

		
	@pytest.mark.parametrize("num, expected", testData + testBigData)
	def test_solution3(self, num, expected):
		assert fibonacci.solution3(num) == expected

		
	@pytest.mark.parametrize("num, expected", testData + testBigData)
	def test_solution4(self, num, expected):
		assert fibonacci.solution4(num) == expected 