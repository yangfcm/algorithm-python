'''
  Given an array of integers representing the color of each sock, determine how
  many pairs of socks with matching colors there are. 
  For example, there are n = 7 socks with colors arr=[1,2,1,2,1,3,2]. 
  There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. 
  So the number of pairs is 2.
'''
def solution(arr):
  pairs = 0
  socksMap = {}
  for n in arr:
    if socksMap.get(n) == None:
      socksMap[n] = 1
    else:
      socksMap[n] += 1
  
  for v in socksMap.values():
    pairs += v // 2
  return pairs
    