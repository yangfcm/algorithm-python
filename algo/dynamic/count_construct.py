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

def solution2(target, strs, memo = None):
  if memo is None: memo = {}
  if target in memo: return memo[target]
  if target == '': return 1
  totalcount = 0
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      totalcount += solution2(sub, strs, memo)
      memo[target] = totalcount
  return totalcount

def solution3(target, strs):
  test_arr = [0] * (len(target) + 1)
  test_arr[0] = 1

  for i in range(len(target)):
    for s in strs:
      if target[i:i+len(s)] == s and i + len(s) <= len(target):
        test_arr[i+len(s)] += test_arr[i]
  
  return test_arr[len(target)]
  
