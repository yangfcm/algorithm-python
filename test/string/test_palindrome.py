import pytest
from algo.string import palindrome

class TestPalindrome:
  testTrueData = [
    ('racecar'),
    ('Rotator'),
    ('solos')
  ]

  testFalseData = [
    ('cars'),
    ('hello')
  ]

  @pytest.mark.parametrize("str", testTrueData)
  def test_solution_true(self, str):
    assert palindrome.solution(str) == True

  @pytest.mark.parametrize("str", testFalseData)
  def test_solution_false(self, str):
    assert palindrome.solution(str) == False
