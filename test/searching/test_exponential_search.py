import pytest
from algo.searching import exponential_search

class TestExponentialSearch:
  testArr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
  testFoundData = [
    (10, 0),
    (16, 3),
    (23, 9),
    (42, 13),
    (47, 14)
  ]

  @pytest.mark.parametrize("dataToSearch, expected", testFoundData)
  def test_solution_found(self, dataToSearch, expected):
    assert exponential_search.solution(self.testArr, dataToSearch) == expected
  
  def test_solution_not_found(self):
    assert exponential_search.solution(self.testArr, 17) == -1