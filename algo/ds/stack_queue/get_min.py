'''
 Given a stack. Find out its minimum number.
 (All elements in stack are number) 
'''
from collections import deque

def solution(stack = deque()):
  tempStack = deque()
  min = None
  while len(stack) > 0:
    item = stack.popleft()
    if min is None or item < min:
      min = item
    tempStack.appendleft(item)
  
  while len(tempStack) > 0:
    stack.appendleft(tempStack.popleft())
  return min
