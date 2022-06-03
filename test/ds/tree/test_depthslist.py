import pytest 

from algo.ds.tree.bst import Node
from algo.ds.tree import depthslist


@pytest.fixture
def bt():
  node = Node(1)
  node.left = Node(2)
  node.right = Node(3)
  node.left.left = Node(4)
  node.left.right = Node(5)
  node.right.left = Node(6)
  node.left.left.left = Node(7)
  node.left.left.left.right = Node(8)
  return node

def test_depthslist(bt):
  lists = depthslist.solution(bt)
  assert lists[0][0].data == 1
  assert lists[1][0].data == 2
  assert lists[1][1].data == 3
  assert lists[2][0].data == 4
  assert lists[2][1].data == 5
  assert lists[2][2].data == 6
  assert lists[3][0].data == 7
  assert lists[4][0].data == 8