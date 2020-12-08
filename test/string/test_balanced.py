import pytest
from algo.string import balanced

class TestBalanced:
  testFalseData = [
    ("}{"),
    ("{}}"),
    ("foo { bar { baz }"),
    ("foo { bar } }")
  ]

  testTrueData = [
    ("{}{}"),
    ("foo { bar { baz } boo }")
  ]

  @pytest.mark.parametrize("str", testTrueData)
  def test_solution_true(self, str):
    assert balanced.solution(str) == True
  
  @pytest.mark.parametrize("str", testFalseData)
  def test_solution_false(self, str):
    assert balanced.solution(str) == False