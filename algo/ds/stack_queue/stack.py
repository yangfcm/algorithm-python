'''
  Stack: A data structure with Last-In-First-Out
  Create a stack data structure and implement its methods like 'add', 'remove', 'peek' and 'empty'
  Example:
    const s = Stack();
    s.push(1);
    s.push(2);
    s.pop();  // returns 2
    s.pop();  // returns 1
'''

class Stack:
  def __init__(self):
    self.__stack = []
  
  def push(self, data):
    self.__stack.append(data)
    return None

  def pop(self):
    return self.__stack.pop()

  def size(self):
    return len(self.__stack)
  
  def isempty(self):
    return self.size() == 0
  
  def peek(self):
    if self.isempty(): return None
    return self.__stack[self.size() - 1]