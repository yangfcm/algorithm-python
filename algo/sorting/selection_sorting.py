'''
Implement selection sorting
 From i=0 to i<array length
 --Assume the element at 'i' is the least in the array, assign i to 'indexOfMin'
 --For j from i+1 to the end of array
 ----See if there is an element with smaller value
 ------If there is, record its index
 --If the index of the current element and the index of the 'smallest' element is not the same, swap them.
'''
def solution(arr):
  for i in range(len(arr)):
    indexOfMin = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[indexOfMin]:
        indexOfMin = j
    if indexOfMin != i:
      arr[i], arr[indexOfMin] = arr[indexOfMin], arr[i]
  return arr