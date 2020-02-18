import contextlib
import unittest 
from algo.math import fizzbuzz
from io import StringIO

class FizzbuzzTest(unittest.TestCase):
	def test_fizzbuzz_arg_5(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			fizzbuzz.solution(5)
		output = temp_stdout.getvalue().strip()
		expected_output = """1
2
fizz
4
buzz"""
		self.assertEqual(output, expected_output)

	def test_fizzbuzz_arg_15(self):
		temp_stdout = StringIO()
		with contextlib.redirect_stdout(temp_stdout):
			fizzbuzz.solution(15)
		output = temp_stdout.getvalue().strip()
		expected_output = """1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz"""
		self.assertEqual(output, expected_output)
	