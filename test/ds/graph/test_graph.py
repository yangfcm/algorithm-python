import pytest 

from algo.ds.graph.graph import Graph

class TestGraph:

  def test_init(self):
    graph = Graph([1,2,3,4,5])
    assert graph.getDirected() == False
    assert graph.getVertexList() == [1,2,3,4,5]
    assert graph.getNumberOfEdges() == 0
    assert graph.getNumberOfVertex() == 5
    assert graph.getMatrix() == [
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]
    ]