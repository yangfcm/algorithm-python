import pytest
from algo.string import count_vowels

class TestCountVowels:
  testData = [
    ("aeiou", 5),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5),
    ("bcdfghjkl", 0),
    ("I like to eat cheese.", 9)
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert count_vowels.solution(str) == expected

    