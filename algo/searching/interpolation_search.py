def solution(arr, val):
  return searchHelper(arr, val, 0 ,len(arr)-1)

def searchHelper(arr, val ,low, high):
  if low < high and val >= arr[low] and val <= arr[high]:
    pos = low + (val - arr[low]) * (high - low) // (arr[high] - arr[low]);
    if arr[pos]==val:
      return pos
    elif arr[pos] < val:
      return searchHelper(arr, val, pos+1, high)
    elif arr[pos] > val:
      return searchHelper(arr, val, low, pos-1)
  return -1