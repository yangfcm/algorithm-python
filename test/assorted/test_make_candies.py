import pytest
from algo.assorted import make_candies

class TestMakeCandies:
  testData = [
    (3, 1, 2, 12, 3),
    (5184889632, 5184889632, 20, 10000, 1),
    (1, 1, 6, 45, 16),
    (1, 2, 343, 270, 135),
    (5, 1, 172, 364, 72)
  ]

  @pytest.mark.parametrize("m, w, p, n, expected", testData)
  def test_solution(self, m, w, p, n, expected):
    assert make_candies.solution(m, w, p, n) == expected