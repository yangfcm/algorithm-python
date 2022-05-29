'''
  Write a function best_sum(target, numbers) that takes in a target sum and an array of numbers as arguments
  The function should return an tuple containing the shortest combination of numbers that add up to exactly the target sum.
  If there is more than one shortest combinations, return any one of them.
  You may use an element of the tuple as many times as needed.
  Assum all input numbers are non-negative.
'''
def solution1(target, numbers):
  if target == 0: return ()
  if target < 0: return None
  best = None
  for n in numbers:
    remainder = target - n
    remainderResult = solution1(remainder, numbers)
    if not remainderResult is None:
      remainderResult += (n,)
      if best is None or len(remainderResult) < len(best):
        best = remainderResult
  return best


def solution2(target, numbers, memo = None):
  if memo is None: memo = {}
  if target in memo: return memo[target]
  if target == 0: return ()
  if target < 0: return None
  best = None
  
  for n in numbers:
    remainder = target - n
    remainderResult = solution2(remainder, numbers, memo)
    if not remainderResult is None:
      remainderResult += (n,)
      if best is None or len(remainderResult) < len(best):
        best = remainderResult
  memo[target] = best
  return best
  

def solution3(target, numbers):
  pass
