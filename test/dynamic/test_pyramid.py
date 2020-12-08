import pytest
from algo.dynamic import pyramid


def test_pyramid_with_number_2(capfd):
  pyramid.solution(2)
  expected_output = """ # 
###
"""
  out,err = capfd.readouterr()
  assert out == expected_output

def test_pyramid_with_number_3(capfd):
  pyramid.solution(3)
  expected_output = """  #  
 ### 
#####
"""
  out,err = capfd.readouterr()
  assert out == expected_output


def test_pyramid_with_number_4(capfd):
  pyramid.solution(4)
  expected_output = """   #   
  ###  
 ##### 
#######
"""
  out,err = capfd.readouterr()
  assert out == expected_output


def test_pyramid_with_number_5(capfd):
  pyramid.solution(5)
  expected_output = """    #    
   ###   
  #####  
 ####### 
#########
"""
  out,err = capfd.readouterr()
  assert out == expected_output