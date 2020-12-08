import pytest
from algo.string import one_away

class TestOneAway:
  testTrueData = [
    ('pale', 'pales'),
    ('pale', 'pal'),
    ('pale', 'bale'),
    ('pales', 'pals'),
    ('pales', 'pales')
  ]

  testFalseData = [
    ('pale', 'bake'),
    ('johnson', 'john'),
    ('pale', 'pad')
  ]

  @pytest.mark.parametrize("str1, str2", testTrueData)
  def test_solution_true(self, str1, str2):
    assert one_away.solution(str1, str2) == True

  @pytest.mark.parametrize("str1, str2", testFalseData)
  def test_solution_false(self, str1, str2):
    assert one_away.solution(str1, str2) == False