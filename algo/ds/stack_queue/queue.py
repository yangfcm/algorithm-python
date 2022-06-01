'''
  Queue
  Quere is a data structure with elements First-In-First-Out
  Create a queue data structure and implement the methods 'add', 'remove', 'peek' etc.
  Example:
  const q = Queue();
  q.add(1);
  q.add(2)
  q.remove();  // return 1
  q.remove(); // return 2
 '''
class Queue:
  def __init__(self):
    self.__queue__ = []
  
  def add(self, data):
    self.__queue__.append(data)

  def remove(self):
    return self.__queue__.pop(0)

  def size(self):
    return (len(self.__queue__))

  def isempty(self):
    return self.size() == 0

  def peek(self):
    if self.isempty(): return None
    return self.__queue__[0]