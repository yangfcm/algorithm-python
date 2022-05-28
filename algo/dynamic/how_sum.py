'''
 Write a function how_sum(target, numbers) that takes in a target sum and an array of numbers as arguments
 The function should return an tuple containing any (one) combination of elements that add up to exactly the target sum.
 If there is no combination that adds up to the target sum, return None.
 You may use an element of the tuple as many times as needed.
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

def solution2(target, numbers, memo = None):
  if memo is None: memo = {}
  if target in memo: return memo[target]
  if target == 0: return ()
  if target < 0: return None

  for n in numbers:
    remainder = target - n
    remainderResult = solution2(remainder, numbers, memo)
    if not remainderResult is None:
      remainderResult += (n,)
      memo[target] = remainderResult
      return memo[target]
  
  memo[target] = None
  return None

def solution3(target, numbers):
  sum_arr = [None] * (target + 1)
  sum_arr[0] = ()

  for i in range(target):
    if not sum_arr[i] is None:
      for n in numbers:
        if i + n <= target:
          sum_arr[i+n] = sum_arr[i] + (n,)
  return sum_arr[target]