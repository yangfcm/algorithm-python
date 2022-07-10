import pytest
from algo.sorting import fradulent_activity_notice

class TestFradulentActivityNotice:
  testData = [
    ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5 ,2)
  ]

  @pytest.mark.parametrize("expenditure, d, expected", testData)
  def test_solution(self, expenditure, d, expected):
    assert fradulent_activity_notice.solution(expenditure, d) == expected