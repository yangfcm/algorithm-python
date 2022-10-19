import pytest
from algo.greedy import greedy_florist

class TestGreedyFlores:
  testData = [
    ([2, 5, 6], 3, 13),
    ([2, 5, 6], 2, 15),
    ([1, 3, 5, 7, 9], 3, 29)
  ]

  @pytest.mark.parametrize("costs, k, expected", testData)
  def test_solution(self, costs, k, expected):
    assert greedy_florist.solution(costs, k) == expected