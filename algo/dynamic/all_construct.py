'''
 Write a function all_construct(target, strs) that accepts a target string and an array of strings.
 The function should return a 2D array containing all of the ways that the target can be
 constructed by concatenating elements of the strs array.
 You may use elements in strs as many times as needed.
 e.g. all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl' ]) ->  [['purp','le'], ['p','ur','p','le']]
'''
def solution1(target, strs):
  if target == '': return [[]]
  constructs = []
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      subconstructs = solution1(sub, strs)
      targetconstructs = []
      targetconstructs = [[s]+ construct for construct in subconstructs]
      print(constructs, targetconstructs)
      constructs += targetconstructs
  return constructs

def solution2(target, strs):
  pass

def solution3(target, strs):
  pass