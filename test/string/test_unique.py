import pytest
from algo.string import unique

class TestOneAway:
  testTrueData = [ 
    ('abcdefg'),
    ('holiday'),
    ('澳大利亚')
  ]

  testFalseData = [
    ('abcda'),
    ('mississippi')
  ]

  @pytest.mark.parametrize("str", testTrueData)
  def test_solution_true(self, str):
    assert unique.solution(str) == True

  @pytest.mark.parametrize("str", testFalseData)
  def test_solution_false(self, str):
    assert unique.solution(str) == False