'''
  Implement a method to perform basic string compression using the counts of repeated characters.
  Example: aabcccccaaa -> a2b1c5a3.
  If the compressed string would not be smaller than the original string, should return original string.
  Assume the string has only uppercase and lowercase letters a-z.
'''
def solution(myStr):
  compressed = ''
  repeatChar = myStr[0]
  repeatCharCnt = 1
  myStr += ' '
  for c in myStr[1:]:
    if c == repeatChar:
      repeatCharCnt += 1
    else:
      compressed += repeatChar + str(repeatCharCnt)
      repeatChar = c
      repeatCharCnt = 1
  
  return compressed if len(compressed) < len(myStr.strip()) else myStr.strip()