import pytest
from algo.string import string_rotation

class TestStringRotation:
  testTrueData = [
    ('waterbottle', 'erbottlewat'),
    ('abcdefg', 'defgabc') 
  ]

  testFalseData = [
    ('waterbottlee', 'erbottlewat'),
    ('waterbottle', 'erbotllewat'),
    ('waterbottle', '')
  ]

  @pytest.mark.parametrize("str1, str2", testTrueData)
  def test_solution_true(self, str1, str2):
    assert string_rotation.solution(str1, str2) == True

  @pytest.mark.parametrize("str1, str2", testFalseData)
  def test_solution_false(self, str1, str2):
    assert string_rotation.solution(str1, str2) == False