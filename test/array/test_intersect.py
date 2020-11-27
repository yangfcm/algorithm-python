import pytest
from algo.array import intersect

class TestIntersect:
  testData = [
    ([4,9,5], [9,4,9,8,4], [4,9]),
    ([1, 1, 1, -2, -2, 5, 8, 9], [1, 1, -2, 9, 10], [1, 1, -2, 9]),
    ([1,2,3,4,5,6,7], [1,1,2,2,2,4], [1,2,4])
  ]

  @pytest.mark.parametrize("arr1, arr2, expected", testData)
  def test_solution(self, arr1, arr2, expected):
    assert intersect.solution(arr1, arr2) == expected