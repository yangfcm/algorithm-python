# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# 	 e.g. Input: [1,2,3]
# 	 Output: [1,2,4]
# 	 Explanation: The array represents the integer 123
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