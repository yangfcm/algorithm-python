import pytest
from algo.searching import binary_search

class TestBinarySearch:
  testArr = [-5, -1, 0, 2, 12, 23, 38, 72, 91, 1001]
  testFoundData = [
    (-5, 0),
    (0, 2),
    (23, 5),
    (91, 8),
    (1001, 9)
  ]

  @pytest.mark.parametrize("dataToSearch, expected", testFoundData)
  def test_solution_found(self, dataToSearch, expected):
    assert binary_search.solution(self.testArr, dataToSearch) == expected
  
  def test_solution_not_found(self):
    assert binary_search.solution(self.testArr, 35) == -1