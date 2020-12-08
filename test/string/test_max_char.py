import pytest
from algo.string import max_char

class TestMaxChar:
  testData =[
    ('abcdefghijklmnaaaaa', 'a'),
    ('ab1c1d1e1f1g1', '1')
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert max_char.solution(str) == expected
