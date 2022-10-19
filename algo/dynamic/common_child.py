'''
  Common Child: A string is considered to be a child of another string if it can be formed by deleting 0 or more characters from the other string.
  Given two strings of equal length, find out the longest string that can be constructed such that it is a child of both.
  Example: s1 = 'ABCD', s2 = 'ABDC'. These two strings have two children with maximum length 3.
  They are 'ABC' and 'ABD'. They can be formed by eliminating either D or C from both strings.
  Explanation: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
'''
def solution(s1, s2):
  table = [ [0] * (len(s2) + 1) for i in range(len(s1) + 1)]
  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      if s1[i-1] == s2[j-1]:
        table[i][j] = table[i-1][j-1] + 1
      else:
        table[i][j] = max(table[i-1][j], table[i][j-1])
  return table[len(s1)][len(s2)]