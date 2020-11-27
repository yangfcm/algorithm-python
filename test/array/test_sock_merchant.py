import pytest
from algo.array import sock_merchant

class TestSockMerchant:
  testData = [
    ([10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
    ([1, 2, 1, 2, 1, 3, 2], 2),
    ([1,2,3,4,5,6], 0)
  ]

  @pytest.mark.parametrize("arr, expected", testData)
  def test_solution(self, arr, expected):
    assert sock_merchant.solution(arr) == expected