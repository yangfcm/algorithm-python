import pytest

from algo.dynamic import can_sum

class TestCanSum:

  def test_solution1(self):
    assert can_sum.solution1(7, [2, 3]) == True
    assert can_sum.solution1(7, [5, 3, 4, 7]) == True
    assert can_sum.solution1(7, [2, 4]) == False
    assert can_sum.solution1(8, [2, 3, 5]) == True