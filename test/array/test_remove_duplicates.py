import pytest
from algo.array import remove_duplicates

class TestRemoveDuplicates:
  testData = [
    ([ 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 ], [ 0, 1, 2, 3, 4 ]),
    ([ -5, -1, -1, 0, 2, 2, 4, 5, 5 ], [-5, -1, 0, 2, 4, 5]),
    ([3, 3, 3, 3, 0, 0, -2, -2], [3, 0, -2]),
    ([1,1,1,1,1,1,1], [1]),
    ([1,2,3,4,5], [1,2,3,4,5])
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution(self, arr, expected):
    assert remove_duplicates.solution(arr) == len(expected)
    assert arr == expected 