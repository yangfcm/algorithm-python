import pytest
from algo.string import make_anagrams

class TestMakeAnagrams: 
  testData = [
    ("cde", "abc", 4),
    ("showman", "woman", 2),
    ("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke", 30)
  ]

  @pytest.mark.parametrize("str1, str2, expected", testData)
  def test_solution(self, str1, str2, expected):
    assert make_anagrams.solution(str1, str2) == expected