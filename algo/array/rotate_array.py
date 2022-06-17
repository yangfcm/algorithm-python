'''
  Given an array, rotate the array to the right by k steps, where k is non-negative.
  Example:  [1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]
  The 1st rotate: [7, 1, 2, 3, 4, 5, 6](The last number 7 is moved to the top of the array)
  The 2nd rotate: [6, 7, 1, 2, 3, 4, 5](Then, the last number 6 is moved to the top of the array)
  The 3rd rotate: [5, 6, 7, 1, 2, 3, 4].
'''
def solution(arr, k):
  count = len(arr)
  for _ in range(k):
    last = arr[count-1]
    arr.pop(count-1)
    arr.insert(0, last)
  return arr