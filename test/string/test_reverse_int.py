import pytest
from algo.string import reverse_int

class TestReverseInt:
  testData =[
    (5, 5),
    (500, 5),
    (2834, 4382),
    (-6, -6),
    (-2834, -4382),
    (-600, -6)
  ]

  @pytest.mark.parametrize("num, expected", testData)
  def test_solution(self, num, expected):
    assert reverse_int.solution(num) == expected
