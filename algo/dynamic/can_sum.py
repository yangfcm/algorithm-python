'''
  Write a function can_sum(target, numbers) that takes in a target sum and an array of numbers as arguments
  The function should return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array.
  
  You may use an element of the array as many times as needed.
  Assum numbers are all non-negative.
'''
from math import remainder


def solution1(target, numbers):
  if target == 0: return True
  if target < 0: return False

  for n in numbers:
    remainder = target - n
    if(solution1(remainder, numbers)): return True

  return False


def solution2(target, numbers):
  pass

def solution3(target, numbers):
  pass