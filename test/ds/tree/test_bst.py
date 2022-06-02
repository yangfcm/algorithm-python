import pytest

from algo.ds.tree.bst import Node

@pytest.fixture
def bstFixture():
  node = Node(10)
  node.insert(5)
  node.insert(15)
  node.insert(12)
  node.insert(2)
  node.insert(4)
  node.insert(1)
  node.insert(14)
  return node

# After the above operation, the BST looks like:
#           10
#          /  \
#         5   15
#        / \  / \
#       2  N 12  N
#      / \   /\  
#     1  4  N 14

def test_bst_node(bstFixture):
  node = bstFixture
  assert node.data == 10
  assert node.left.data == 5
  assert node.right.data == 15
  assert node.left.left.data == 2
  assert node.left.right == None
  assert node.right.left.data == 12
  assert node.right.right == None
  assert node.left.left.left.data == 1
  assert node.left.left.right.data == 4
  assert node.right.left.left == None
  assert node.right.left.right.data == 14

def test_contain(bstFixture):
  assert bstFixture.contain(10).data == 10
  assert bstFixture.contain(1).data == 1
  assert bstFixture.contain(14).data == 14
  assert bstFixture.contain(12).data == 12
  assert bstFixture.contain(0) == None