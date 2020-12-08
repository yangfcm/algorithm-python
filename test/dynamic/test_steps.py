import pytest
from algo.dynamic import steps

def test_steps_with_number_3(capfd):
  steps.solution(3)
  expected_output = """#  
## 
###
"""
  out,err = capfd.readouterr()
  assert out == expected_output

def test_steps_with_number_4(capfd):
  steps.solution(4)
  expected_output = """#   
##  
### 
####
"""
  out,err = capfd.readouterr()
  assert out == expected_output