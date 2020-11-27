import pytest
from algo.array import plus_one

class TestPlusOne:
  testData = [
    ([1,2,3], [1,2,4]),
    ([1,9,9,9], [2,0,0,0]),
    ([9,9,9,9], [1,0,0,0,0]),
    ([3, 6, 1, 2, 2, 9], [3, 6, 1, 2, 3, 0])
  ]

  @pytest.mark.parametrize("digits, expected", testData)
  def test_solution(self, digits, expected):
    assert plus_one.solution(digits) == expected