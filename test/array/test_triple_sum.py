import pytest
from algo.array import triple_sum

class TestTripleSum:
  testData = [
    ([1, 3, 5], [2, 3], [1, 2, 3], 8),
    ([1, 4, 5], [2, 3, 3], [1, 2, 3], 5),
    ([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13], 12)
  ]

  @pytest.mark.parametrize("a, b, c, expected", testData)
  def test_solution(self, a, b, c, expected):
    assert triple_sum.solution(a, b, c) == expected