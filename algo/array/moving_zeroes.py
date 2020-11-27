# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#  In-place operation
#  e.g. Input: [0,1,0,3,12]
# Output: [1,3,12,0,0] 
def solution(arr):
  countZero = arr.count(0)
  for _ in range(countZero):
    arr.remove(0)
    arr.append(0)
  return arr
