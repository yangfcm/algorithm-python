'''
  Accept a positive number n The function should print a pyramid shape with n levels using # character. 
  Make sure the step has spaces on both left and right side.

  Example:
    2 =>
    ' # '
    '###'
    3 =>
    '  #  '
    ' ### '
    '#####'
    4 =>
    '   #   '
    '  ###  '
    ' ##### '
    '#######'
'''

def solution(n):
  for i in range(1,n+1):
    print(('#'*(2*i-1)).center(2*n-1, ' '))