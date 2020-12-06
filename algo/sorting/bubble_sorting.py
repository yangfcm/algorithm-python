'''
Implement bubble sorting
  Bubble sorting:
  From i=0 to i<array length
  --From j=0 to (array length - i)
  ----If the element at j is greater than its next element(j+1)
  ------Swap elements j and j+1
'''
def solution(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr