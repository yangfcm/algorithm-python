'''
Implement hash table class
'''

class HashTable:
  def __init__(self, size = 8):
    if size <= 0: raise ValueError('Size must be a positive integer')
    self.table = [[]] * size
    self.count = 0
    self.size =size
  
  def __hash__(self, key):
    return abs(hash(key)) % self.size 

  def put(self, key, value):
    index = self.__hash__(key)
    bucket = self.table[index]

    for i, node in enumerate(bucket, start = 0):  # See if there's conflicting key. If there is, overwrite it.
      if node[0] == key:
        bucket[i] = (key, value)
        return value
    
    bucket.append((key, value))
    self.count += 1

    if(self.count > self.size * .75):
      self.__resize__(self.size * 2)
    return value

  def get(self, key):
    index = self.__hash__(key)
    bucket = self.table[index]
    for node in bucket:
      if node[0] == key: return node[1]
    return None

  def remove(self, key):
    index = self.__hash__(key)
    bucket = self.table[index]
    for i, node in enumerate(bucket, start=0):
      if node[0] == key:
        bucket.pop(i)
        self.count -= 1
        if self.count < self.size * .25:
          self.__resize__(self.size // 2)
        return node[1]
    return None

  def __resize__(self, newSize):
    oldTable = self.table
    self.size = newSize
    self.count = 0
    self.table = [[]] * newSize

    for bucket in oldTable:
      for node in bucket:
        self.put(node[0], node[1])