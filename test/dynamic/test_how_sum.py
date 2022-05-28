import pytest

from algo.dynamic import how_sum

class TestHowSum:

  def test_solution1(self):
    assert how_sum.solution1(7, [2, 3]) == (3,2,2)
    assert how_sum.solution1(7, [5, 3, 4, 7]) == (4,3)
    assert how_sum.solution1(7, [2, 4]) == None
    assert how_sum.solution1(8, [2, 3, 5, 6]) == (2,2,2,2)

  def test_solution2(self):
    assert how_sum.solution2(7, [2, 3]) == (3,2,2)
    assert how_sum.solution2(7, [5, 3, 4, 7]) == (4,3)
    assert how_sum.solution2(7, [2, 4]) == None
    assert how_sum.solution2(8, [2, 3, 5, 6]) == (2,2,2,2)
    assert how_sum.solution2(300, [7,14]) == None
    assert how_sum.solution2(300, [14,286]) == (14, 286)
    
  
  def test_solution2(self):
    assert how_sum.solution3(7, [2, 3]) == (3,2,2)
    assert how_sum.solution3(7, [5, 3, 4, 7]) == (4,3)
    assert how_sum.solution3(7, [2, 4]) == None
    assert how_sum.solution3(8, [2, 3, 5, 6]) == (2,2,2,2)
    assert how_sum.solution3(300, [7,14]) == None
    assert how_sum.solution3(300, [14,286]) == (286, 14)