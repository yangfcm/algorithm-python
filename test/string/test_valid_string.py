import pytest 
from algo.string import valid_string

class TestValidString:
  testData = [
    ('abcd', True),
    ('abcdefghhgfedecba', True),
    ('aaabbbccccddd', True),
    ('aabbccddeefghi', False),
    ('aaabbbbcccdddd', False),
    ('aabbcd', False)
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert valid_string.solution(str) == expected