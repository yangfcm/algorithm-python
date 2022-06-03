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
    self.__isVisited__ = [] * self.__numberOfVertex__
    self.__graphArr__ = []
  
  def insertEdge(start, end, weight = 1):
    pass

  def removeEdge(start, end):
    pass

  def getFirstAdjacent(self, v):
    pass

  def getNextAdjacent(self, v1, v2):
    pass

  def traverseBFS(self):
    pass

  def traverseDFS(self):
    pass

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