'''
Given a string, return true or false to indicate whether the string has balanced brackets.
Brackets can be '[]', '{}', or '()'
'''
from algo.ds.stack_queue.stack import Stack

def solution(str):
  bracketStack = Stack()

  for ch in str:
    if(ch == '(' or ch == '{' or ch == '['):
      bracketStack.push(ch)
    
    if(
      (ch == ')' and bracketStack.peek() != '(') or
      (ch == '}' and bracketStack.peek() != '{') or
      (ch == ']' and bracketStack.peek() != '[')
    ):
      return False
    
    if(
      (ch == ')' and bracketStack.peek() == '(') or
      (ch == '}' and bracketStack.peek() == '{') or
      (ch == ']' and bracketStack.peek() == '[')
    ):
      bracketStack.pop()
    
  return bracketStack.isempty()