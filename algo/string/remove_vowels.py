'''
Given a string, remove the vowels from the string and return the string without vowels
'''
def solution(str):
  vowels = 'aeiouAEIOU'
  strWithoutVowel = ''
  for c in str:
    if not c in vowels:
      strWithoutVowel += c
  return strWithoutVowel