import pytest
from algo.greedy import min_absolute_diff

class TestMinAbsoluteDiff:
  testData = [
    ([3, -7, 0], 3),
    ([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75], 1),
    ([1, -3, 71, 68, 17], 3)
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution(self, arr, expected):
    assert min_absolute_diff.solution(arr) == expected