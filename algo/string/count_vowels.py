'''
Return the number of vowels used in a string 
e.g.!-- "apple" => 2 "why?" => 0
'''
def solution(str):
  vowels = 'aeiouAEIOU'
  cnt = 0
  for c in str:
    if c in vowels:
      cnt += 1
  return cnt