'''
Take a string and return true or false to indicate whether its curly braces are balanced 
e.g. '}{' - false 
  '{abc}{def}' - true 
  '{abc {def}}' - true 
  'abc {def}}' - false
'''
def solution(str):
  cnt = 0
  for c in str:
    if c == '{':
      cnt += 1
    if c == '}':
      cnt -= 1
    if cnt < 0:
      # If a closing bracket doesn't have a matching opening bracket, return false early
      return False
  
  return cnt == 0