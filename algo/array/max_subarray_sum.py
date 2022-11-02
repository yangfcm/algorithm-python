'''
  Max Subarray Sum: Given an integer array, find the contiguous subarray which has the largest sum and return its sum.
  The array should contain positive number and negative number.

  Example: arr = [-2,1,-3,4,-1,2,1,-5,4] -> 6 (The subarray is [4, -1, 2, 1], 4 + (-1) + 2 + 1 = 6)
'''

# Brutal force comparison.
import math

def solution1(arr):
  maxSum = None
  for i in range(len(arr)):
    sum = arr[i]
    if maxSum == None or sum > maxSum: maxSum = sum
    for n in arr[(i+1):]:
      sum += n 
      if sum > maxSum: maxSum = sum
  return maxSum

# Kadane's algorithm: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def solution2(arr):
  maxSoFar = -math.inf
  maxEndingHere = 0

  for num in arr:
    maxEndingHere += num
    if maxEndingHere > maxSoFar: maxSoFar = maxEndingHere
    if maxEndingHere < 0: maxEndingHere = 0
  
  return maxSoFar
