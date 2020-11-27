import pytest
from algo.array import is_sorted

class TestIsSorted:
  testSortedData = [
    ([1,2,3,4,5]),
    ([1,5,9,100,1001,9999])
  ]

  testUnsortedData = [
    ([1,2,4,5,4]),
    ([5,4,3,2,1,0,-2]),
    ([1,100,1001,0,9999,99999])
  ]

  @pytest.mark.parametrize("sorted", testSortedData)
  def test_solution_true(self, sorted):
    assert is_sorted.solution(sorted) == True

  @pytest.mark.parametrize("unsorted", testUnsortedData)
  def test_solution_false(self, unsorted):
    assert is_sorted.solution(unsorted) == False