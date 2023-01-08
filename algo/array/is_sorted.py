'''
  Given an array of numbers, return true or false, indicating whether the array is sorted.
'''
def solution(arr):
  if len(arr) == 0:
    return True
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True