
from algo.dynamic import best_sum

class TestBestSum:

  def test_solution1(self):
    assert best_sum.solution1(7, [2, 3]) == (3,2,2)
    assert best_sum.solution1(7, [5, 3, 4, 7]) == (7,)
    assert best_sum.solution1(7, [2, 4]) == None
    assert best_sum.solution1(8, [2, 3, 5, 6]) == (6,2)