'''
 Write a function can_construct(target, strs) that accepts a target string and an array of strings.
 The function should return a boolean indicating whether or not the target can be
 constructed by concatenating elements of the strs array.
 You may use elements in strs as many times as needed.
 e.g. You can use elements in ["ab", "abc", "cd", "def", "abcd"] to construct string "abcdef" ("abc" + "def"), so function returns true
 But there is no way to construct "abcef", so function returns false.
'''
def solution1(target, strs):
  if target == '': return True
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      if solution1(sub, strs): return True
  return False

def solution2(target, strs, memo = None):
  if memo is None: memo = {}
  if target in memo: return memo[target]
  if target == '': return True
  for s in strs:
    if target.startswith(s):
      sub = target[len(s):]
      if solution2(sub, strs, memo):
        memo[target] = True
        return True
  memo[target] = False
  return False
  

def solution3(target, strs):
  test_arr = [False] * (len(target) + 1)
  test_arr[0] = True

  for i in range(len(target)):
    if test_arr[i]:
      for s in strs:
        if target[i:i+len(s)] == s and i + len(s) <= len(target):
          test_arr[i+len(s)] = True
  return test_arr[len(target)]