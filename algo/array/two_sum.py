# Given an array of integers, return indices of the two numbers such that they
#  add up to a specific target. Assume each input would have excactly one
#  solution and you cannot use the same element twice 
#  e.g. Given nums = [2, 7, 11, 15], target = 9 Because nums[0] + nums[1] = 2 + 7 = 9 return [0, 1]
def solution(arr, target):
  dic = {}
  for i in range(len(arr)):
    complement = target - arr[i]
    if dic.get(complement) != None:
      return [dic.get(complement), i]
    dic[arr[i]] = i
  return None