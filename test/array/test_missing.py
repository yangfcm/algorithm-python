import pytest
from algo.array import missing

class TestMissing:
  testData = [
    ([1,4,3,5,6], 2),
    ([2,5,4,3,1], None),
    ([], None)
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution(self, arr, expected):
    assert missing.solution(arr) == expected