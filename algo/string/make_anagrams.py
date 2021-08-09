'''
makeAnagrams: Given two strings, str1 and str2, determine the minimum number of characters deletions
required to make str1 and str2 anagrams. The strings str1 and str2 consist of lowercase English letters [a-z].
e.g. makeAnagrams('abcd','dcefg') -> 5
explanation: delete a, b from 'abcd' and delete e,f,g from 'dcefg' to make 'cd' and 'dc', which are anagrams. That is 5 deletions.
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''

def solution( str1, str2):
  deletions = 0
  letters = 'abcdefghijklmnopqrstuvwxyz'
  strDict1 = {}
  strDict2 = {}
  for c in str1:
    strDict1[c] = strDict1.get(c, 0) + 1
  for c in str2:
    strDict2[c] = strDict2.get(c, 0) + 1
  for l in letters:
    deletions += abs(strDict1.get(l, 0) - strDict2.get(l, 0))
  return deletions
