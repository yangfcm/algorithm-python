'''
Permutations: Given an array of distinct integers, return all the possible permutations.

Example: arr = [1, 2, 3]
It has permutations: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

'''
def solution(arr):
  permutations = []

  if len(arr) == 0: return []
  if len(arr) == 1: return [arr]

  for i in range(len(arr)):
    remainingNums = arr[0:i] + arr[i+1:]
    remainingNumsPermuted = solution(remainingNums)
    for j in range(len(remainingNumsPermuted)):
      permutations.append([arr[i], *remainingNumsPermuted[j]])

  return permutations