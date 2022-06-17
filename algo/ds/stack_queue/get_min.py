'''
  Given a stack. Find out its minimum number.
  (All elements in stack are number) 
'''
from algo.ds.stack_queue.stack import Stack

def solution(stack = Stack()):
  tempStack = Stack()
  min = stack.peek()
  while stack.size() > 0:
    item = stack.pop()
    if min is None or item < min:
      min = item
    tempStack.push(item)
  
  while tempStack.size() > 0:
    stack.push(tempStack.pop())
  return min
