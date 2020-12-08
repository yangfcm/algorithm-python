import pytest
from algo.string import string_compress

class TestStringCompress:
  testData =[
    ('aaaaaaaaaaaa', 'a12'),
    ('xxxxxxyyyxxzzzyz', 'x6y3x2z3y1z1'),
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcdefg', 'abcdefg'),
    ('xxxxyxxzzzyz', 'xxxxyxxzzzyz'),
    ('xxyyz','xxyyz')
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert string_compress.solution(str) == expected
