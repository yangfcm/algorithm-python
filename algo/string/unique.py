'''
  Given a string, determine if it has all unique characters. 
  Solution: Use a list to record the characters in the string. 
  If the character appears before, return false. Otherwise, add the character to the list 
  Then iterate the object to see if there is a character with the count > 1
'''
def solution(str):
  chars = []
  for c in str:
    if c in chars:
      return False
    else:
      chars.append(c)
  return True
  