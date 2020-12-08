import pytest
from algo.string import capitalize

class TestCapitalize:
  testData = [
    ("hi there, how is it going?", "Hi There, How Is It Going?"), 
    ("i love breakfast at bill miller bbq", "I Love Breakfast At Bill Miller Bbq")
  ]
 
  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert capitalize.solution(str) == expected
   