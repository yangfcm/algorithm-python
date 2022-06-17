'''
  Take an unsorted array of unique numbers from 1 to n.
  Return the missing number in the sequence or null if there is no missing number
  There is either no missing number or exactly one missing number.
  Example: [1, 4, 3, 5] -> 2
  [2, 3, 4, 1] -> null
  [] -> null
'''
def solution(arr):
  if len(arr) == 0:
    return None
  maxNumber = max(arr)
  sumNumber = sum(arr)
  expectedSum = maxNumber * (maxNumber+1) / 2;
  diff = expectedSum - sumNumber
  return None if diff == 0 else diff