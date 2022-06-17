'''
  Given a string, check if it is a permutation of a palindrome.
  Check is case insensitive.
  Example: Test TactCoa should return true because it has permutations: "tacocat", "atcocta", which are palindromes.
  Of course, it is impossible to generate all permutations of a string and test if it is a palindrome one by one.
  To solve this, create a character map, with key is the characters of the string and value is the occurence of the character.
  If the string is a permutation of a palindrome, it must have at most one character that has appeared in the string odd-number times.
'''
def solution(str):
  charMap = {}
  for c in str.lower():
    if c == ' ': 
      continue
    charMap[c] = charMap.get(c, 0) + 1
  
  oddCnt = 0
  for k,v in charMap.items():
    if v % 2 != 0:
      oddCnt += 1
    if oddCnt > 1:
      return False
  
  return True