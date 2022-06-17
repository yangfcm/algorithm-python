def solution(arr):
  if len(arr) == 1:
    return arr
  
  # split the array into two half ones
  middle = len(arr)//2
  left = arr[0:middle]
  right = arr[middle:len(arr)]

  # Recursively split the left arrays and right arrays until they both have one element left.
  # And then merge them into a sorted array.
  return mergeHelper(solution(left), solution(right))

def mergeHelper(left, right):
  merged = []
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      merged.append(left.pop(0))
    else:
      merged.append(right.pop(0))
  return [*merged, *left, *right]