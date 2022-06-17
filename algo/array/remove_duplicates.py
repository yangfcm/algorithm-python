'''
  Given a sorted array nums, remove the duplicates in-place* such that each element appear only once and return the new length.
  Example: Given nums = [0,0,1,1,1,2,2,3,3,4], return length = 5 
'''
def solution(arr):
  if len(arr) == 0: 
    return 0
  for i in range(len(arr)-1, 0, -1):
    if arr[i] == arr[i-1]:
      arr.pop(i)
  return len(arr)
