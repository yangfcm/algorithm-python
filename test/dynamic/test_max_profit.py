import pytest
from algo.dynamic import max_profit

class TestMaxProfit:
  testData = [
    ([7, 1, 5, 3, 4, 6, 4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
    ([1,2,5,7,2,1], 6)
  ]

  @pytest.mark.parametrize('prices, expected', testData)
  def test_solution(self, prices, expected):
    assert max_profit.solution(prices) == expected