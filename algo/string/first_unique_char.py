'''
  First Unique Character: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

  Example: "leetcode" -> 0 (letter l is the first character, whose index is 0)
  "loveleetcode" -> 2 (letter v)
  "aabb" -> -1 (No unique character)
  Use a character map(object) to record the number of each character.
  Then iterate each character in the string, for the first character whose count is 1, return its index; otherwise return -1 (no unique character)
'''
def solution(str):
  charMap = {}
  for c in str:
    charMap[c] = charMap.get(c, 0) + 1
  
  for i, ch in enumerate(str):
    if charMap.get(ch) == 1:
      return i
  
  return -1