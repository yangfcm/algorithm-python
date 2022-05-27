'''
 Write a function how_sum(target, numbers) that takes in a target sum and an array of numbers as arguments
 The function should return an array containing any (one) combination of elements that add up to exactly the target sum.
 If there is no combination that adds up to the target sum, return None.
 You may use an element of the array as many times as needed.
 Assum all input numbers are non-negative.
'''
def solution1(target, numbers):
  if target == 0: return ()
  if target < 0: return None
  for n in numbers:
    remainder = target - n
    remainderResult = solution1(remainder, numbers)
    if not remainderResult is None:
      remainderResult += (n,)
      return remainderResult
  return None

def solution2(target, numbers):
  pass

def solution3(target, numbers):
  pass