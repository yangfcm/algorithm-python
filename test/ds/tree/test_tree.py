import pytest 

from algo.ds.tree.tree import Node, traverseBFS, traverseDFS

def test_node_initialization():
  n = Node('a')
  assert n.data == 'a'
  assert len(n.children) == 0

def test_node_add_remove():
  n = Node('a')
  n.add('b')
  n.add('c')
  n.add('d')
  assert n.children[0].data == 'b'
  assert n.children[1].data == 'c'
  assert n.children[2].data == 'd'
  n.remove('b')
  assert n.children[0].data == 'c'
  assert n.children[1].data == 'd'
  n.remove('c')
  assert n.children[0].data == 'd'

@pytest.fixture
def treeFixture():
  tree = Node('a')
  tree.add('b')
  tree.add('c')
  tree.add('d')
  tree.children[0].add('e')
  tree.children[0].add('f')
  tree.children[2].add('g')
  tree.children[2].add('h')
  return tree

def test_traverse_bfs(treeFixture):
  traverseList = traverseBFS(treeFixture)
  assert traverseList == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def test_traverse_dfs(treeFixture):
  traverseList = traverseDFS(treeFixture)
  assert traverseList == ['a', 'b', 'e', 'f', 'c', 'd', 'g', 'h']