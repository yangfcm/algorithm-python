import pytest

from algo.ds.stack_queue import largest_rectangle

class TestLargestRectangle:
  testData = [
    ([1, 2, 3, 4, 5], 9),
    ([2, 1, 5, 6, 2, 3], 10),
    ([11, 11, 10, 10, 10], 50),
    ([1, 3, 5, 9, 11], 18)
  ]

  @pytest.mark.parametrize("heights, expected", testData)
  def test_solution(self, heights, expected):
    assert largest_rectangle.solution(heights) == expected

