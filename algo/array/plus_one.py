'''
  Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
  Example: plusOne([1,2,3]) -> [1,2,4]
  plusOne([1, 9, 9]) -> [2, 0, 0]
  plusOne([9, 9, 9]) -> [1, 0, 0, 0]
'''
def solution(digits):
  for i in range(len(digits)-1, -1, -1):
    if digits[i] < 9:
      digits[i] += 1
      return digits
    if digits[i] == 9:
      digits[i] = 0
      if i == 0:
        digits.insert(0, 1)
  return digits