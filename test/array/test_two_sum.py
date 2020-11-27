import pytest
from algo.array import two_sum

class TestTwoSum:
  testData = [
    ([2,7,11,15,99,12,34], 110, [2,4]),
    ([2,7,11,15,99,12,34], 36, [0,6])
  ]

  @pytest.mark.parametrize("arr, target, expected", testData)
  def test_solution(self, arr, target, expected):
    assert two_sum.solution(arr, target) == expected