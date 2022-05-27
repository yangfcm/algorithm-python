import pytest

from algo.dynamic import grid_traveler

class TestGridTraveler: 
  smallTestData = [
    (1, 1, 1),
    (2, 3, 3),
    (3, 2, 3),
    (3, 3, 6),
    (12, 13, 1352078),
  ]

  testData = smallTestData + [
    (18, 18, 2333606220)
  ]

  @pytest.mark.parametrize("m, n, expected", smallTestData)
  def test_solution1(self, m, n, expected):
    assert grid_traveler.solution1(m, n) == expected

  @pytest.mark.parametrize("m, n, expected", testData)
  def test_solution1(self, m, n, expected):
    assert grid_traveler.solution2(m, n) == expected
    assert grid_traveler.solution3(m, n) == expected
