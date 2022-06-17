'''
  Accept a positive number n The function should console write a step shape with n levels using # character. 
  Make sure the step has spaces on the right side.
  Example:  
    2 =>
    '# '
    '##'
    3 =>
    '#  '
    '## '
    '###'
    4 =>
    '#   '
    '##  '
    '### '
    '####'
'''
def solution(n):
  for i in range(1, n+1):
    print(('#'*i).ljust(n, ' '))