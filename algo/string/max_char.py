'''
Give a string, return the character that is most commonly used in the string
'''
def solution(str):
  strMap = {} 
  for c in str:
    strMap[c] = strMap.get(c, 0) + 1  
  
  maxCnt = 0
  maxChar = ''
  for k,v in strMap.items():
    if v > maxCnt:
      maxCnt = v
      maxChar = k
  return maxChar