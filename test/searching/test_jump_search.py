import pytest
from algo.searching import jump_search

class TestExponentialSearch:
  testArr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
  testFoundData = [
    (0, 0),
    (1, 1),
    (5, 5),
    (55, 10),
    (233, 13),
    (610, 15)
  ]

  @pytest.mark.parametrize("dataToSearch, expected", testFoundData)
  def test_solution_found(self, dataToSearch, expected):
    assert jump_search.solution(self.testArr, dataToSearch) == expected
  
  def test_solution_not_found(self):
    assert jump_search.solution(self.testArr, 17) == -1
    assert jump_search.solution(self.testArr, 1000) == -1