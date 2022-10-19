'''
  Max Min: Given an array of integers and a single integer k, create an array of length k from
  elements of arr such that its difference is minimized.

  Example: arr = [10, 100, 300, 200, 1000, 20, 30], k = 3 -> 20
  Choose k = 3 elements from arr: [10, 20, 30] where the maximum is 30 and the minimum is 10 and their difference is 20.
'''
def solution(arr, k):
  arr.sort()  # sort arr from smallest to biggest
  minDiff = None
  for i in range(len(arr) - k): # Get the subarray by k length
    diff = arr[i+k-1] - arr[i]

    if minDiff == None or (minDiff != None and diff < minDiff):
      minDiff = diff
  return minDiff
