'''
Implement hash table class
'''

class HashTable:
  def __init__(self, size = 8):
    if size <= 0: raise ValueError('Size must be a positive integer')
    self.__table__ = [[]] * size
    self.__count__ = 0
    self.__size__ =size
  
  def __hash__(self, key):
    return abs(hash(key)) % self.__size__ 

  def put(self, key, value):
    index = self.__hash__(key)
    bucket = self.__table__[index]

    for i, node in enumerate(bucket, start = 0):  # See if there's conflicting key. If there is, overwrite it.
      if node[0] == key:
        bucket[i] = (key, value)
        return value
    
    bucket.append((key, value))
    self.__count__ += 1

    if(self.__count__ > self.__size__ * .75):
      self.__resize__(self.__size__ * 2)
    return value

  def get(self, key):
    index = self.__hash__(key)
    bucket = self.__table__[index]
    for node in bucket:
      if node[0] == key: return node[1]
    return None

  def remove(self, key):
    index = self.__hash__(key)
    bucket = self.__table__[index]
    for i, node in enumerate(bucket, start=0):
      if node[0] == key:
        bucket.pop(i)
        self.__count__ -= 1
        if self.__count__ < self.__size__ * .25:
          self.__resize__(self.__size__ // 2)
        return node[1]
    return None

  def __resize__(self, newSize):
    oldTable = self.__table__
    self.__size__ = newSize
    self.__count__ = 0
    self.__table__ = [[]] * newSize

    for bucket in oldTable:
      for node in bucket:
        self.put(node[0], node[1])

  def count(self):
    return self.__count__

  def size(self):
    return self.__size__