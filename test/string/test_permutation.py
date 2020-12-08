import pytest
from algo.string import permutation

class TestOneAway:
  testTrueData = [
    ('abcdefg', 'dgfebca'),
    ('abcdefg', 'gfedcba'),
    ('abcdefg', 'cgfeabd')
  ]

  testFalseData = [
    ('abcdefg', 'abcdefgg'),
    ('abcdefg', 'bcdefg'),
    ('abcdefg', 'degfacd')
  ]

  @pytest.mark.parametrize("str1, str2", testTrueData)
  def test_solution_true(self, str1, str2):
    assert permutation.solution(str1, str2) == True

  @pytest.mark.parametrize("str1, str2", testFalseData)
  def test_solution_false(self, str1, str2):
    assert permutation.solution(str1, str2) == False