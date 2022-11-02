'''
  Max Subarray Mod Sum: Given a positive integer array nums and an integer m, find the contiguous subarray which has the largest sum mod m.
  Example: arr = [3, 3, 9, 9, 5] m = 7 -> 6 ( 3%7 + 3%7 = 6)
'''
import bisect
import itertools
import math

# Brutal force comparison.
def solution1(arr, m):
  maxSum = -math.inf
  for i in range(len(arr)):
    sum = arr[i] % m
    if sum > maxSum: maxSum = sum

    for n in arr[i+1:]:
      sum = (sum + n) % m
      if sum > maxSum: maxSum = sum
  return maxSum

def solution2(arr, m):
  a = list(map(lambda x:x%m, itertools.accumulate(arr)))
  maxi = max(a)
  ar = []
  for i in a:
    bisect.insort(ar,i)
    if i!=ar[-1]:
      maxi = max(maxi,(i-ar[bisect.bisect_right(ar,i)])%m)
  return maxi