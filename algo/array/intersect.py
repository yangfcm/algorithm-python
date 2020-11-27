# Given two arrays, write a function to compute their intersection.
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# e.g. Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]     
def solution(arr1, arr2): 
  smaller = arr1 if len(arr1) < len(arr2) else arr2
  bigger = arr1 if len(arr1) >= len(arr2) else arr2
  intersect = []
  for n in smaller:
    try:
      foundIndex = bigger.index(n)
      intersect.append(n)
      bigger.pop(foundIndex)
    except:
      continue
  return intersect