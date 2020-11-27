import pytest
from algo.array import rotate_array

class TestRotateArray:
  testData = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3,99,-1,-100]),
    ([1,2,3,4,5,6,7], 1, [7,1,2,3,4,5,6])
  ]

  @pytest.mark.parametrize("arr, k, expected", testData)
  def test_solution(self, arr, k, expected):
    assert rotate_array.solution(arr, k) == expected