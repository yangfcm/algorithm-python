import pytest
from algo.string import reverse_string

class TestReverseString:
  testData =[
    ('abcde', 'edcba'),
    ('my test', 'tset ym')
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert reverse_string.solution(str) == expected
