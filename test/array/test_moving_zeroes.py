import pytest
from algo.array import moving_zeroes

class TestMovingZeroes:
  testData = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([-5, 0, 0, 3, 0, 0, 0, 0], [-5, 3, 0, 0, 0, 0, 0, 0]),
    ([1,2,3,4,0,6,7], [1,2,3,4,6,7,0])
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution(self, arr, expected):
    assert moving_zeroes.solution(arr) == expected