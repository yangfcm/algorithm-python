import pytest
from algo.string import palindrome_permutation

class TestPalindromePermutation:
  testTrueData = [
    ('Tact Coa'),
    ('aaaabbbbbbccdde'),
    ('jjkjkjkkabcabc')
  ]

  testFalseData = [
    ('abcdabcdcd')
  ]

  @pytest.mark.parametrize("str", testTrueData)
  def test_solution_true(self, str):
    assert palindrome_permutation.solution(str) == True

  @pytest.mark.parametrize("str", testFalseData)
  def test_solution_false(self, str):
    assert palindrome_permutation.solution(str) == False
