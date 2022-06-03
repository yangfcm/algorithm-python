import pytest 

from algo.ds.graph.graph import Graph

@pytest.fixture
def directedGraph():
  dg = Graph([1,2,3,4,5], True)
  dg.insertEdge(0, 1)
  dg.insertEdge(1, 3)
  dg.insertEdge(2, 3)
  dg.insertEdge(2, 4)
  dg.insertEdge(0, 4)
  dg.insertEdge(4, 0)
  return dg

@pytest.fixture
def undirectedGraph():
  udg = Graph([1,2,3,4,5], False)
  udg.insertEdge(0, 1)
  udg.insertEdge(1, 3)
  udg.insertEdge(2, 3)
  udg.insertEdge(2, 4)
  udg.insertEdge(0, 4)
  return udg
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
  
  def test_directed_graph_insert_remove_edge(self):
    graph = Graph([1,2,3,4,5], True)
    graph.insertEdge(0, 1)
    assert graph.getNumberOfEdges() == 1
    assert graph.getMatrix()[0][1] == 1
    assert graph.getMatrix()[1][0] == 0
    graph.insertEdge(2, 4, 9)
    assert graph.getNumberOfEdges() == 2
    assert graph.getMatrix()[2][4] == 9
    assert graph.getMatrix()[4][2] == 0
    graph.removeEdge(2, 4)
    assert graph.getNumberOfEdges() == 1
    assert graph.getMatrix()[2][4] == 0
    assert graph.getMatrix()[4][2] == 0    

  def test_undirected_graph_insert__remove_edge(self):
    graph = Graph([1,2,3,4,5], False)
    graph.insertEdge(0, 1)
    assert graph.getNumberOfEdges() == 1
    assert graph.getMatrix()[0][1] == 1
    assert graph.getMatrix()[1][0] == 1
    graph.insertEdge(2, 4, 9)
    assert graph.getNumberOfEdges() == 2
    assert graph.getMatrix()[2][4] == 9
    assert graph.getMatrix()[4][2] == 9
    graph.removeEdge(2, 4)
    assert graph.getNumberOfEdges() == 1
    assert graph.getMatrix()[2][4] == 0
    assert graph.getMatrix()[4][2] == 0

  def test_BFS_traverse(self, directedGraph, undirectedGraph):
    assert directedGraph.traverseBFS() == [1,2,5,4,3]
    assert undirectedGraph.traverseBFS() == [1,2,5,4,3]

  def test_DFS_traverse(self, directedGraph, undirectedGraph):
    assert directedGraph.traverseDFS() == [1,2,4,5,3]
    assert undirectedGraph.traverseDFS() == [1,2,4,3,5]