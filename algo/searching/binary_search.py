'''
 Implement binary search
 Given a sorted array, search a given element val in the array
'''
def solution(arr, val):
  return searchHelper(arr, val, 0, len(arr))

def searchHelper(arr, val, start, end):
  if end >= start:
    mid = (start+end)//2
    if arr[mid] == val:
      # The element is found
      return mid
    elif val > arr[mid]:
      # If the element to find is larger than the middle element,
      # Continue searching in the upper half of array
      return searchHelper(arr, val, mid+1, end)
    elif val < arr[mid]:
      # If the element to find is smaller than the middle element,
      # Continue searching in the lower half of array
      return searchHelper(arr, val, start, mid-1)
  return -1