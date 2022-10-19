import pytest
from algo.string import special_string

class TestSpecialString:
  testData = [
    ('aaaa', 10),
    ('abcbaba', 10),
    ('asasd', 7),
    ('abcde', 5)
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert special_string.solution(str) == expected