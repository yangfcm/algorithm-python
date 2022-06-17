'''
  Validate a given string is palindrome
'''
def solution(str):
  return str.lower() == str[::-1].lower()