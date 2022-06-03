'''
Implement hash table class
'''

class HashTable:
  def __init__(self, size = 8):
    self.table = [[]] * size
    self.count = 0
    self.size =size
  
  def __hash__(self, key):
    return abs(hash(key)) % self.size 

  def put(self, key, value):
    index = self.__hash__(key)
    bucket = self.table[index]

    for i, node in enumerate(bucket, start = 0):
      if node[0] == key:
        bucket[i] = (key, value)
        return value
    
    bucket.append((key, value))
    self.count += 1

    if(self.count > self.size * .75):
      self.resize(self.size * 2)
    return value

  def get(self, key):
    index = self.__hash__(key)
    bucket = self.table[index]
    if len(bucket) == 0: return None
    for node in bucket:
      if node[0] == key: return node[1]
    return None

  def remove(self, key):
    pass

  def resize(self, newSize):
    pass
