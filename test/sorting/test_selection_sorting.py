import pytest
from algo.sorting import selection_sorting

class TestSelectionSorting:
  testData = [
    ([ 100, -40, 500, -124, 0, 21, 7], [-124, -40, 0, 7, 21, 100, 500])
  ]

  @pytest.mark.parametrize("arr, sorted", testData)
  def test_solution(self, arr, sorted):
    assert selection_sorting.solution(arr) == sorted