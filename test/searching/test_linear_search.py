import pytest
from algo.searching import linear_search

class TestLinearSearch:
  testArr = [10, 20, 80, 30, 60, 50, 11, 100, 130, 170]
  testFoundData = [
    (10, 0),
    (80, 2),
    (50, 5),
    (130, 8),
    (170, 9)
  ]

  @pytest.mark.parametrize("dataToSearch, expected", testFoundData)
  def test_solution_found(self, dataToSearch, expected):
    assert linear_search.solution(self.testArr, dataToSearch) == expected
    
  def test_solution_not_found(self):
    assert linear_search.solution(self.testArr, 35) == -1