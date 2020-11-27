#	Return true or false, indicating whether a given array of numbers is sorted
def solution(arr):
  if len(arr) == 0:
    return true
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True