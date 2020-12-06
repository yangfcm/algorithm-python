import pytest
from algo.sorting import merge_sorting

class TestMergeSorting:
  testData = [
    ([ 100, -40, 500, -124, 0, 21, 7], [-124, -40, 0, 7, 21, 100, 500])
  ]

  @pytest.mark.parametrize("arr, sorted", testData)
  def test_solution(self, arr, sorted):
    assert merge_sorting.solution(arr) == sorted