import pytest 

from algo.ds.tree import bst_val
from algo.ds.tree.bst import Node

@pytest.fixture
def bst():
  node = Node(10)
  node.insert(5)
  node.insert(15)
  node.insert(12)
  node.insert(2)
  node.insert(4)
  node.insert(1)
  node.insert(14)
  return node

def test_bst_val(bst):
  assert bst_val.solution(bst) == True

def test_non_bst_val(bst):
  bst.right.right = Node(0) # Break the bst
  assert bst_val.solution(bst) == False
  