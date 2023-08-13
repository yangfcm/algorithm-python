import pytest
from algo.string import defanging_ip

class TestDefangingIP:
  testData = [
    ("1.1.1.1", "1[.]1[.]1[.]1"),
    ("255.100.50.0", "255[.]100[.]50[.]0")
  ]

  @pytest.mark.parametrize("ip, expected", testData)
  def test_solution(self, ip, expected):
    assert defanging_ip.solution(ip) == expected