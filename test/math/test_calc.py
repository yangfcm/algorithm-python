import pytest 
from algo.math import calc

def test_add(): 
	result = calc.add( 10,5)
	assert result == 15
	