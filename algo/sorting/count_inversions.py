def solution1(arr):
  count = 0
  for i in range(len(arr)):
    if i == 0: continue
    for n in arr[i-1::-1]:
      if n > arr[i]: 
        count += 1
  return count

count = 0
def mergeSort(arr):
  if len(arr) == 1:
    return arr
  
  # split the array into two half ones
  middle = len(arr)//2
  left = arr[0:middle]
  right = arr[middle:]

  # Recursively split the left arrays and right arrays until they both have one element left.
  # And then merge them into a sorted array.
  return mergeHelper(mergeSort(left), mergeSort(right))

def mergeHelper(left, right):
  global count
  merged = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      merged.append(left.pop(0))
    else:
      count += len(left)
      merged.append(right.pop(0))
  return [*merged, *left, *right]

def solution2(arr):
  global count
  count = 0
  mergeSort(arr)
  return count