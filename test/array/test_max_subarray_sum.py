import pytest  
from algo.array import max_subarray_sum

class TestMaxSubArraySum:
  testData = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([38, -9, 23, -13, 9, 5, 12, -8, 90, -32, 53, -85, 34, 59, -12, -93], 176),
    ([-9, -3, 5, -10, 3], 5)
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution1(self, arr, expected):
    assert max_subarray_sum.solution1(arr) == expected
    
  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution2(self, arr, expected):
    assert max_subarray_sum.solution2(arr) == expected