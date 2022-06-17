'''
  Return an integer in reverse
  Example: reverseInt(521) = 125, reverseInt(-521) = -125, reverseInt(1200) = 21
'''
def solution(num):
  reversedInt = int(str(abs(num))[::-1])
  return reversedInt if num > 0 else reversedInt*-1