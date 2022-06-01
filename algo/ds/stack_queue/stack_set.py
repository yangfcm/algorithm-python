'''
  Imagine a (literal) stack of plates. If the stack goes too high, it might topple.
  Therefore, in real life, we would start a new stack when the previous stack exceeds a threshold.
  Implement a data structure StackSet to mimic this.
  StackSet should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
  StackSet.push() and StackSet.pop() should behave identically to a single stack
  Also implement a function popAt(index) to perform pop operation on a particular sub-stack.
  Think about the sub-stack is not at full capacity when pop an element from it.
'''
from algo.ds.stack_queue.stack import Stack

class StackSet:
  def __init__(self, capacity):
    if capacity <= 0: raise Exception('Invalid value for capacity. Capacity must be a positive integer.')
    self.__capacity__ = capacity
    self.__stacks__ = Stack() # It's a stack of stack.
  
  def getCapacity(self):
    return self.__capacity__

  def push(self, data):
    if self.__stacks__.isempty():
      self.__stacks__.push(Stack())
    
    lastStack = self.__stacks__.peek()  # We are about to push new data to the last stack
    if lastStack.size() >= self.__capacity__: # Check if the last stack is full.
      newStack = Stack()  # If it's full, need to create a new stack.
      newStack.push(data)
      self.__stacks__.push(newStack)
    else:
      lastStack.push(data)

  def pop(self):
    if self.__stacks__.isempty(): return None
    lastStack = self.__stacks__.peek()
    elToPop = lastStack.pop() # Pop an element from the last stack
    if(lastStack.isempty()):  # Check if the last stack is empty
      self.__stacks__.pop() # If empty, pop it too.
    return elToPop

  '''
    This is a bit trickier to implement, but we can imagine a "rollover" system. 
    
    If we pop an element from stack 1, we need to remove the bottom of stack 2 and push it onto stack 1. 
    We then need to rollover from stack 3 to stack 2, stack 4 to stack 3, etc.

    You could make an argument that, rather than "rolling over;' it should be okay with some stacks not
    being at full capacity. This would improve the time complexity (by a fair amount, with a large number of
    elements), but it might get us into tricky situations later on if someone assumes that all stacks (other than
    the last) operate at full capacity. There's no "right answer" here; you could start a discussion about this trade-off
    In this implementation, the sub-stack will be removed only when it gets empty.
  '''
  def popat(self, index):
    pass

  def peek(self):
    if self.__stacks__.isempty(): return None
    return self.__stacks__.peek().peek()

  def peekat(self, index):  # Peek the element of a stack with a given index.
    if index < 0: raise Exception('Invalid value for index.')
    if self.size() <= index: return None
    tempStacks = Stack()
    for i in range(self.__stacks__.size()-index):
      print(i)
      tempStacks.push(self.__stacks__.pop())
    
    elToPeek = tempStacks.peek().peek()
    while tempStacks.size() > 0:
      self.__stacks__.push(tempStacks.pop())
        
    return elToPeek

  def size(self): # Returns how many stacks in the set, not how many elements in the stack set.
    return self.__stacks__.size()
  