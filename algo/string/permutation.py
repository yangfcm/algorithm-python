'''
  Check if one string is a permutation of another. Solution: Create character maps for both str1 and str2 and compare them. 
  If each character has the same value(count of characters), they are permutation, otherwise, they are not.
'''
def solution(str1, str2):
  strMap1 = {}
  strMap2 = {}
  for c in str1:
    strMap1[c] = strMap1.get(c, 0) + 1
  
  for c in str2:
    strMap2[c] = strMap2.get(c, 0) + 1
  
  if len(strMap1) != len(strMap2):
    return False
  
  for k,v in strMap1.items():
    if strMap1.get(k) != strMap2.get(k):
      return False
  return True
