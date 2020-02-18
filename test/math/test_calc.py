import unittest 
from algo.math import calc

class CalcTest(unittest.TestCase):
	def test_add(self): 
		result = calc.add( 10,5)
		self.assertEqual(result, 15)
	