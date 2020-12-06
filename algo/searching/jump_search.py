import math

def solution(arr, val):
  length = len(arr)
  last = length - 1
  step = math.floor(math.sqrt(length))
  start = 0
  end = start + step - 1
  while arr[min(end, last)] < val:
    start += step
    end += step
    if start > last:
      return -1
  
  for i in range(start, min(end, last)+1):
    if arr[i] == val:
      return i
  
  return -1