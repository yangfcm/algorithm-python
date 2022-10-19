import pytest
from algo.dynamic import common_child

class TestCommonChild:
  testData = [
    ("AA", "BB", 0),
    ("HARRY", "SALLY", 2),
    ("SHINCHAN", "NOHARAAA", 3),
    ("OUDFRMYMAW", "AWHYFCCMQX", 2),
    (
      "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS",
      "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC",
      15,
    ),
  ]

  @pytest.mark.parametrize("s1, s2, expected", testData)
  def test_solution(self, s1, s2, expected):
    assert common_child.solution(s1, s2) == expected