import unittest 
from algo.math import is_prime

class IsPrimeTest(unittest.TestCase):
	def test_0_is_not_a_prime(self):
		self.assertFalse(is_prime.solution(0))
	def test_1_is_not_a_prime(self):
		self.assertFalse(is_prime.solution(1))
	def test_2_is_not_a_prime(self):
		self.assertFalse(is_prime.solution(2))
	def test_3_is_a_prime(self):
		self.assertTrue(is_prime.solution(3))
	def test_17_is_a_prime(self):
		self.assertTrue(is_prime.solution(17))
	def test_10000_is_not_a_prime(self):
		self.assertFalse(is_prime.solution(10000))

	