import pytest
from algo.assorted import min_time

class TestMinTime:
  testData = [
    ([2, 2], 2, 2),
    ([2, 3], 5, 6),
    ([1, 3, 4], 10, 7),
    ([4, 5, 6], 12, 20)
  ]

  @pytest.mark.parametrize("machines, goal, expected", testData)
  def test_solution(self, machines, goal, expected):
    assert min_time.solution(machines, goal) == expected
