'''
  Given two arrays, compute their intersection.
  Each element in the result should appear as many times as it shows in both arrays.
  The result can be in any order.
  Example: nums1 = [4,9,5], nums2 = [9,4,9,8,4], intersect(nums1, nums2) -> [4, 9]
  nums1 = [1, 1, 1, -2, -2, 5, 8, 9], nums2 = [1, 1, -2, 9, 10], intersect(nums1, nums2) -> [1, 1, -2, 9]
  nums1 = [2, 3, 4], nums2 = [5, 6, 7], intersect(nums1, nums2) -> []
'''
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