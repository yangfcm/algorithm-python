'''
 Capitalize:
 Give a string, capitalize the first letter of each word in the string then return the capitalized string.
 e.g. it is so good --> It Is So Good
'''
def solution(str):
  return ' '.join([w.capitalize() for w in str.split(' ')])