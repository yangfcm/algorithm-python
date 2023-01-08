import pytest

from algo.ds.stack_queue import is_balanced

class TestIsBalanced:
  testTrueData = [
    "{[()]}",
    "{{[[(())]]}}",
    "{(([])[])[]}",
    "{(([])[])[]}[]",
    "abcd"
  ]

  testFalseData = [
    "{[(])}",
    "{(([])[])[]]}",
    "(abcd"
  ]

  @pytest.mark.parametrize("str", testTrueData)
  def test_solution_true(self, str):
    assert is_balanced.solution(str) == True
  
  @pytest.mark.parametrize("str", testFalseData)
  def test_solution_false(self, str):
    assert is_balanced.solution(str) == False