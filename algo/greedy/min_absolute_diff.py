'''
  Minimum Absolute Difference: Given an array of integers, find the minimum absolute difference between any two elements in the array.
  Example: arr = [1, -3, 71, 68, 17] -> 3 (|71-68|= 3)
'''
def solution(arr):
  minDiff = None
  arr.sort()

  for v, next in zip(arr, arr[1:]):
    diff = next - v
    if minDiff == None or diff < minDiff:
      minDiff = diff
  
  return minDiff
