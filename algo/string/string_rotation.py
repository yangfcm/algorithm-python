'''
Given two strings, check if s2 is a rotation of s1 using only one call to isSubstring.
If a string is a rotation of another, it's a rotation at a particular point.
e.g. a rotation of "waterbottle" at character 3 means cutting this string at character 3 and 
putting the right half('erbottle') before the left half('wat') so the result is "erbottlewat"
'''

def solution(str1, str2):
  if len(str1) != len(str2) or len(str1) == 0 or len(str2) == 0:
    return False
  return (str1+str1).find(str2) != -1