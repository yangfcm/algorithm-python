'''
Implement exponential search
'''
from algo.searching import binary_search 

def solution(arr, val):
  if arr[0] == val:
    return 0
  i = 1
  while i < len(arr) and arr[i] <= val:
    i = i*2
  return binary_search.searchHelper(arr, val, i//2, min(i, len(arr)-1))