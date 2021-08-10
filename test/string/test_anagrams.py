import pytest
from algo.string import anagrams

class TestAnagrams:
  testTrueData = [
    ('hello', 'llohe'),
    ('Whoa! Hi!', 'Hi! Whoa!')
  ]

  testFalseData = [
    ("One One", "Two two two"),
    ("One one", "One one cc")
  ]

  @pytest.mark.parametrize("str1, str2", testTrueData)
  def test_solution_true(self, str1, str2):
    assert anagrams.solution(str1, str2) == True
  
  @pytest.mark.parametrize("str1, str2", testFalseData)
  def test_solution_false(self, str1, str2):
    assert anagrams.solution(str1, str2) == False