import pytest

from algo.ds.tree.bst import Node
from algo.ds.tree.btree_traverse import inorderTraverse, preorderTraverse, postorderTraverse

@pytest.fixture
def fixture():
  node1 = Node(1)
  node1.left = Node(2)
  node1.right = Node(3)
  node1.left.left = Node(4)
  node1.left.right = Node(5)

  node2 = Node(25)
  node2.insert(15)
  node2.insert(50)
  node2.insert(10)
  node2.insert(22)
  node2.insert(35)
  node2.insert(70)
  node2.insert(4)
  node2.insert(12)
  node2.insert(18)
  node2.insert(24)
  node2.insert(31)
  node2.insert(44)
  node2.insert(66)
  node2.insert(90)

  return { "node1": node1, "node2": node2 }

def test_preorder_traverse(fixture):
  assert preorderTraverse(fixture["node1"]) == [1, 2, 4, 5, 3]
  assert preorderTraverse(fixture["node2"]) == [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]

def test_inorder_traverse(fixture):
  assert inorderTraverse(fixture["node1"]) == [4, 2, 5, 1, 3]
  assert inorderTraverse(fixture["node2"]) == [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]

def test_postorder_traverse(fixture):
  assert postorderTraverse(fixture["node1"]) == [4, 5, 2, 3, 1]
  assert postorderTraverse(fixture["node2"]) == [4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25]