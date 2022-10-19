'''
  Reverse Shuffle Merge: We define some operations on a string as follows:
  1. Reverse, reverse a string e.g. Reverse 'abc' is 'cba'
  2. Shuffle, shuffle the characters in a string. e.g. Shuffle 'abc' can be 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
  3. Merge, intersperse two strings with maintaining the order of characters in both.
  e.g. Merge 'abc' and 'def' can be 'abcdef', 'adbecf', 'abdefc', 'adefbc' etc.
  Given a string s such that s is one of the results of the operation: merge(reverse(A), shuffle(A)) (A is another string)
  find out the lexicographically smallest(字典排序中最小/前的一個) A

  Example 1: 
  s = eggegg -> egg
  reverse('egg') -> 'gge', shuffle('egg') -> 'egg', 'eggegg' belongs to the merge of ('gge', 'egg')
  Example 2:
  s = abcdefgabcdefg -> agfedcb
  reverse('agfedcb') -> 'bcdefga', shuffle('agfedcb') -> 'abcdefg', 'bcdefgabcdefg' belongs to the merge of ('bcdefga','abcdefg')
'''
def solution(str):
  sortedS = ''.join(sorted(str))
  letterCounts = {}
  letterCountsShuffle = {}
  for i, ch in enumerate(sortedS):
    if i % 2 == 0:
      letterCounts[ch] = letterCounts.get(ch, 0) + 1
    else:
      letterCountsShuffle[ch] = letterCountsShuffle.get(ch, 0) + 1
  
  reversedS = ''.join(reversed(str))
  strArr = []

  for l in reversedS:
    if letterCounts[l] > 0:
      while len(strArr) > 0 and strArr[-1] > l and letterCountsShuffle[strArr[-1]] > 0:
        # Find out the smallest letter available
        removed = strArr.pop()
        letterCountsShuffle[removed] -= 1
        letterCounts[removed] += 1
      strArr.append(l)
      letterCounts[l] -= 1
    else:
      letterCountsShuffle[l] -= 1
  
  return ''.join(strArr)