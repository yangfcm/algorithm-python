'''
  Sort a stack such that the smallest item is on the top.
  You can use an additional temporary stack, but you cannot copy the elements into any other data structure, such as array.
'''

from algo.ds.stack_queue.stack import Stack

def solution(stack = Stack()):
  sortedStack = Stack()
  while stack.size() > 0:
    currentEl = stack.pop()
    if sortedStack.isempty(): sortedStack.push(currentEl)
    else:
      while sortedStack.size() > 0 and sortedStack.peek() > currentEl:
        stack.push(sortedStack.pop())
      sortedStack.push(currentEl)
  
  while sortedStack.size() > 0:
    stack.push(sortedStack.pop())