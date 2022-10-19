import pytest
from algo.greedy import max_min

class TestMaxMin:
  testData = [
    ([10, 100, 300, 200, 1000, 20, 30], 3, 20),
    ([1, 2, 3, 4, 10, 20, 30, 40, 100, 200], 4, 3),
    ([2, 1, 2, 1, 2, 1], 2, 0)
  ]

  @pytest.mark.parametrize("arr, k, expected", testData)
  def test_solution(self, arr, k, expected):
    assert max_min.solution(arr, k) == expected