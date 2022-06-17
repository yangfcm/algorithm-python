'''
  Implement a Queue data structure using two Stacks.
  Queue should implement the methods of add(), remove() and peek()
  Example:
    const q = new QueueFromStack();
    q.add(1);
    q.add(2);
    q.peek();  // returns 1
    q.remove(); // returns 1
    q.remove(); // returns 2
'''
from algo.ds.stack_queue.stack import Stack

class QueueFromStack:
  def __init__(self):
    self.__stack1__ = Stack()
    self.__stack2__ = Stack()

  def add(self, data):
    self.__stack1__.push(data)

  def remove(self):
    while self.__stack1__.size() > 0: # Move all the elements from stack1 to stack2
      self.__stack2__.push(self.__stack1__.pop())
    
    dataToRemove = self.__stack2__.pop()  # Now the top element in stack2 is exactly the one to remove for the queue
    while self.__stack2__.size() > 0:   # Move the rest elements in stack2 back to stack1.
      self.__stack1__.push(self.__stack2__.pop())

    return dataToRemove

  def peek(self):
    while self.__stack1__.size() > 0: # Move all the elements from stack1 to stack2
      self.__stack2__.push(self.__stack1__.pop())
    
    dataToPeek = self.__stack2__.peek()  # Now the top element in stack2 is exactly the one to remove for the queue
    while self.__stack2__.size() > 0:   # Move the rest elements in stack2 back to stack1.
      self.__stack1__.push(self.__stack2__.pop())

    return dataToPeek

  def size(self):
    return self.__stack1__.size()