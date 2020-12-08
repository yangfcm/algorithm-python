import pytest
from algo.string import remove_vowels

class TestRemoveVowels:
  testData =[
    ('hello', 'hll'),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'BCDFGHJKLMNPQRSTVWXYZ'),
    ('Orange', 'rng'),
    ('I love apples and bananas', ' lv ppls nd bnns') 
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert remove_vowels.solution(str) == expected
