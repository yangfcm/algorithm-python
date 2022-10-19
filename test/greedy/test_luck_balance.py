import pytest
from algo.greedy import luck_balance

class TestLuckBalance:
  testData = [
    ([
      [5, 1],
      [2, 1],
      [1, 1],
      [8, 1],
      [10, 0],
      [5, 0],
    ], 3, 29),
    (
      [
        [13, 1],
        [10, 1],
        [9, 1],
        [8, 1],
        [13, 1],
        [12, 1],
        [18, 1],
        [13, 1],
      ], 5, 42
    ),
    (
      [
        [5, 1],
        [4, 0],
        [6, 1],
        [2, 1],
        [8, 0],
      ], 2, 21
    )
  ]

  @pytest.mark.parametrize("contests, k, expected", testData)
  def test_solution(self, contests, k, expected):
    assert luck_balance.solution(contests, k) == expected
