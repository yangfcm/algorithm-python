'''
  Special String: 
    A string is considered to be special if either of two conditions is met:
    1. All the characters are the same, e.g. aaa.
    2. All the characters except the middle one are the same, e.g. aadaa.
    Given a string s, determine how many special substrings can be formed from it.
  Example:
    s = mnonopoo -> It has 12 special substrings, they are: 'm', 'n', 'o', 'n', 'o', 'p', 'o', 'o', 'non', 'ono', 'opo', 'oo'
'''
def solution(str):
  count = len(str)  # Each single character is a special substring.
  
  for i, ch in enumerate(str):  # Count substrings that have exact same characters.
    for nextCh in str[i+1:]:
      if ch == nextCh: count+=1
      else: break

  for i, ch in enumerate(str[:-1]): # Now count the substring that all characters are same except the middle one.
    offset = 1
    next = str[i + offset]
    
    while(i - offset >= 0 and i + offset < len(str)):
      if str[i - offset] == str[i + offset] and next == str[i+offset] and next != ch:
        count += 1
      else: break
      offset += 1

  return count