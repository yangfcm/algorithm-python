import pytest
from algo.array import array_chunk

class TestArrayChunk:
  testData = [
    ([1,2,3,4,5], 1, [[1],[2],[3],[4],[5]]),
    ([1,2,3,4,5], 2, [[1,2,],[3,4],[5]]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 4, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13]]),
    ([1,2,3,4,5], 7, [[1,2,3,4,5]])
  ]

  @pytest.mark.parametrize("arr, size, expected", testData)
  def test_solution(self, arr, size, expected):
    assert array_chunk.solution(arr, size) == expected