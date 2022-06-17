'''
  Write a function all_construct(target, strs) that accepts a target string and an array of strings.
  The function should return a 2D array containing all of the ways that the target can be
  constructed by concatenating elements of the strs array.
  You may use elements in strs as many times as needed.
  Example:
    target = 'purple' strs = ['purp', 'p', 'ur', 'le', 'purpl' ] ->  [['purp','le'], ['p','ur','p','le']
'''
def solution1(target, strs):
  if target == '': return [[]]
  constructs = []
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      subconstructs = solution1(sub, strs)
      targetconstructs = [[s]+ construct for construct in subconstructs]
      constructs += targetconstructs
  return constructs

def solution2(target, strs, memo = None):
  if memo is None: memo = {}
  if target in memo: return memo[target]
  if target == '': return [[]]
  constructs = []
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      subconstructs = solution2(sub, strs, memo)
      targetconstructs = [[s]+ construct for construct in subconstructs]
      constructs += targetconstructs

  memo[target] = constructs
  return constructs

def solution3(target, strs):
  constructs_arr = [[]] * (len(target) + 1)
  constructs_arr[0] = [[]]

  for i in range(len(target)):
    for s in strs:
      if target[i:i+len(s)] == s and i + len(s) <= len(target):
        newconstruct =(construct + [s] for construct in construct_arr[i])
        construct_arr[i + len(s)].append(newconstruct)
  
  return construct_arr[len(target)]