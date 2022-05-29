'''
 Write a function countConstruct(target, strs) that accepts a target string and an array of strings.
 The function should return the number of ways that the target can be
 constructed by concatenating elements of the strs array.
 You may use elements in strs as many times as needed.
 e.g. countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl' ]) -> 2 i.e. 'purp' + 'le', 'p'+'ur'+'p'+'le'
'''
def solution1(target, strs):
  if target == '': return 1
  totalcount = 0
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      totalcount += solution1(sub, strs)
  return totalcount

def solution2(target, strs):
  pass

def solution3(target, strs):
  pass
