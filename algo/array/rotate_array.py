#  Given an array, rotate the array to the right by k steps, where k is non-negative.
#  	 Modify array in-place
#  	 e.g. Input: [1,2,3,4,5,6,7] and k = 3
# 		Output: [5,6,7,1,2,3,4]
def solution(arr, k):
  count = len(arr)
  for _ in range(k):
    last = arr[count-1]
    arr.pop(count-1)
    arr.insert(0, last)
  return arr