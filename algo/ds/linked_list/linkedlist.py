'''
  Implement a linked list
'''

class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.__head__ = None

  def size(self):
    count = 0
    node = self.__head__
    while node != None:
      count+=1
      node = node.next
    return count

  def clear(self):
    self.__head__ = None

  def getfirst(self):
    return self.__head__

  def getlast(self):
    return None if self.size() == 0 else self.get(self.size() - 1)

  def get(self, index): # Return the data at a particular position by index
    if index < 0: raise Exception('Invalid value for in index')
    if index >= self.size(): return None
    node = self.__head__
    for _ in range(index):
      node = node.next
    return node
  
  def insert(self, data, index):
    if index < 0 or index > self.size(): raise Exception('Out of bound')
    if(self.__head__ == None):
      self.__head__ = Node(data)
      return
    
    if index == 0:
      self.__head__ = Node(data, self.__head__)
      return

    previous = self.get(index - 1)
    previous.next = Node(data, previous.next) 

  def insertfirst(self, data):
    self.insert(data, 0)

  def insertlast(self, data):
    if self.size() == 0: 
      self.insertfirst(data)
      return
    self.insert(data, self.size())

  def remove(self, index):
    if index < 0 or index >= self.size(): raise Exception('Out of bound')
    if index == 0:
      self.__head__ = self.__head__.next
      return
    
    node = self.get(index)
    previous = self.get(index - 1)
    previous.next = node.next

  def removefirst(self):
    self.remove(0)

  def removelast(self):
    self.remove(self.size() - 1)