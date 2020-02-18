import unittest
from algo.math import fibonacci

class FibonacciTest(unittest.TestCase):
	def test_fib_arg_1(self):
		self.assertEqual(1, fibonacci.solution1(1))
		self.assertEqual(1, fibonacci.solution2(1))
		self.assertEqual(1, fibonacci.solution3(1))
	def test_fib_arg_2(self):
		self.assertEqual(1, fibonacci.solution1(2))
		self.assertEqual(1, fibonacci.solution2(2))
		self.assertEqual(1, fibonacci.solution3(2))
	def test_fib_arg_3(self):
		self.assertEqual(2, fibonacci.solution1(3))
		self.assertEqual(2, fibonacci.solution2(3))
		self.assertEqual(2, fibonacci.solution3(3))
	def test_fib_arg_4(self):
		self.assertEqual(3, fibonacci.solution1(4))
		self.assertEqual(3, fibonacci.solution2(4))
		self.assertEqual(3, fibonacci.solution3(4))
	def test_fib_arg_20(self):
		self.assertEqual(6765, fibonacci.solution1(20))
		self.assertEqual(6765, fibonacci.solution2(20))
		self.assertEqual(6765, fibonacci.solution3(20))
	def test_fib_art_39(self):
		self.assertEqual(63245986, fibonacci.solution2(39))
		self.assertEqual(63245986, fibonacci.solution3(39))