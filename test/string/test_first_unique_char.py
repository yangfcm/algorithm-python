import pytest
from algo.string import first_unique_char

class TestFirstUniqueChar:
  testData = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabbccc", -1)
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert first_unique_char.solution(str) == expected