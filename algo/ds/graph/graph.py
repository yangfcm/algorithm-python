'''
Implement a graph class
'''
class Graph:
  def __init__(self, vertexList = [], directed = False):
    self.__directed__ = directed
    self.__vertexList__ = vertexList
    self.__numberOfEdges__ = 0
    self.__numberOfVertex__ = len(vertexList)
    self.__matrix__ = [ [0] * self.__numberOfVertex__ for _ in range(self.__numberOfVertex__)]
    self.__isVisited__ = []  # A list to save which vertex is traversed.
    self.__traverseList__ = []   # A list to record the traverse path.
  
  def insertEdge(self, start, end, weight = 1):
    if start < 0 or start >= self.__numberOfVertex__: raise ValueError('Start index is out of bound')
    if end < 0 or end >= self.__numberOfVertex__: raise ValueError('End index is out of bound')
    if type(weight) != int or weight < 0: raise ValueError('Weight must be a positive integer')
    if start == end: return
    if self.__matrix__[start][end] == 0:
      self.__matrix__[start][end] = weight
      if self.__directed__ == False:
        self.__matrix__[end][start] = weight
    self.__numberOfEdges__ += 1
    
  def removeEdge(self, start, end):
    if start < 0 or start >= self.__numberOfVertex__: raise ValueError('Start index is out of bound')
    if end < 0 or end >= self.__numberOfVertex__: raise ValueError('End index is out of bound')
    if start == end: return
    if self.__matrix__[start][end] != 0:
      self.__matrix__[start][end] = 0
      if self.__directed__ == False:
        self.__matrix__[end][start] = 0
    self.__numberOfEdges__ -= 1

  # Given the index of a vertex, find its first adjacent vertex
  def getFirstAdjacent(self, v):
    if v < 0 or v >= self.__numberOfVertex__: raise ValueError('Vertex index is out of bound')
    for i in range(self.__numberOfVertex__):
      if self.__matrix__[v][i] > 0: return i
    return -1

  # Given the index of a vertex(v1), find its first adjacent vertex starting from v2
  def getNextAdjacent(self, v1, v2):
    if v1 < 0 or v1 >= self.__numberOfVertex__ or v2 < 0 or v2 >= self.__numberOfVertex__: 
      raise ValueError('Vertex index is out of bound') 
    for i in range(v2+1, self.__numberOfVertex__):
      if self.__matrix__[v1][i] > 0: return i
    return -1
  
  def getValueByIndex(self, index):
    return self.__vertexList__[index]

  def traverseBFS(self):
    self.__traverseList__ = []
    self.__isVisited__ = [False] * self.__numberOfVertex__
    for i in range(self.__numberOfVertex__):
      if self.__isVisited__[i] == False:
        self.traverseBFSVertex(i)
    return self.__traverseList__

  def traverseBFSVertex(self, index):
    queue = []
    self.__traverseList__.append(self.getValueByIndex(index))
    self.__isVisited__[index] = True
    queue.append(index)
    while len(queue) > 0:
      u = queue.pop(0)
      adjacent = self.getFirstAdjacent(u)
      while adjacent != -1:
        if self.__isVisited__[adjacent] == False:
          self.__traverseList__.append(self.getValueByIndex(adjacent))
          self.__isVisited__[adjacent] = True
          queue.append(adjacent)
        adjacent = self.getNextAdjacent(u, adjacent)

  def traverseDFS(self):
    self.__traverseList__ = []
    self.__isVisited__ = [False] * self.__numberOfVertex__
    for i in range(self.__numberOfVertex__):
      if self.__isVisited__[i] == False:
        self.traverseDFSVertex(i)
    return self.__traverseList__

  def traverseDFSVertex(self, index):
    vertexList = []
    self.__traverseList__.append(self.getValueByIndex(index))
    self.__isVisited__[index] = True
    w = self.getFirstAdjacent(index)
    while w >= 0:
      if self.__isVisited__[w] == False:
        self.traverseDFSVertex(w)
      w = self.getNextAdjacent(index, w)

  def getDirected(self):
    return self.__directed__
  
  def getVertexList(self):
    return self.__vertexList__
  
  def getNumberOfEdges(self):
    return self.__numberOfEdges__
    
  def getNumberOfVertex(self):
    return self.__numberOfVertex__

  def getMatrix(self):
    return self.__matrix__