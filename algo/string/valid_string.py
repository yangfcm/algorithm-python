'''
  Valid String: A string is considered to be valid if all characters of the string appear the same number of times.
  It is also valid if you can remove just 1 character at one index in the string and
  the remaining characters will occur the same number of times.
  Given a string s, determine if it is valid as per the above rule.
  Example:
    s = abc -> valid. Characters all appear once in string.
    s = abcc -> valid. Just remove 'c' and the remaining characters all appear once
    s = abccc -> invalid.
'''
def solution(str):
  charMap = {}
  for c in str:
    charMap[c] = charMap.get(c, 0) + 1
  
  countValues = list(charMap.values())
  if len(countValues) == 1: return True

  countValues.sort()
  first = countValues[0]
  second = countValues[1]
  last = countValues[-1]
  secondLast = countValues[-2]

  if first == last: return True
  if first == 1 and second == last: return True
  if first != 1 and last - secondLast == 1 and secondLast == first: return True

  return False