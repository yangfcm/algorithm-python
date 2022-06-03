import pytest 

from algo.ds.tree.tree import Node
from algo.ds.tree import levelwidth

@pytest.fixture
def tree1():
  node = Node(1)
  node.add(2)
  node.add(3)
  node.add(4)
  node.children[0].add(5)
  node.children[0].add(6)
  node.children[1].add(7)
  node.children[2].add(8)
  return node

@pytest.fixture
def tree2():
  node = Node(1)
  return node

@pytest.fixture
def tree3():
  node = Node(1)
  node.add(2)
  node.add(3)
  node.add(4)
  node.children[0].add(5)
  node.children[0].add(6)
  node.children[1].add(7)
  node.children[2].add(8)
  node.children[0].add(9)
  node.children[2].add(10)
  node.children[0].children[0].add(11)
  node.children[0].children[0].add(12)
  node.children[0].children[0].children[0].add(13)
  return node

def test_solution(tree1, tree2, tree3):
  assert levelwidth.solution(tree1) == [1, 3, 4]
  assert levelwidth.solution(tree2) == [1]
  assert levelwidth.solution(tree3) == [1, 3, 6, 2, 1]