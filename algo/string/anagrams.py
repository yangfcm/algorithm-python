'''
Anagram: Check to see if two provided strings are anagrams of each other. 
One string is an anagram of the other if it uses the same characters in the same quantity. 
Requirements: only conside characters, not spaces or punctuation or number. 
Conside capital letters to be the same as lower case 
e.g. anagrams('rail safety', 'fairy tales') --> true 
 anagrams('RAIL! SAFETY!', 'fairy tales') --> true
 angagrams('Hi, there', 'Bye, there') --> false
'''
def solution(str1, str2):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  strMap1 = {}
  strMap2 = {}
  for c in str1.lower():
    if c in letters:
      strMap1[c] = strMap1.get(c, 0) + 1
  
  for c in str2.lower():
    if c in letters:
      strMap2[c] = strMap2.get(c, 0) + 1
  
  if len(strMap1) != len(strMap2):
    return False
  
  for k,v in strMap1.items():
    if strMap1.get(k) != strMap2.get(k):
      return False

  return True

