import pytest  

from algo.ds.tree import minimal_bst

def test_list_1():
  node = minimal_bst.solution([1,2,3])
  assert node.data == 2
  assert node.left.data == 1
  assert node.right.data == 3

def test_list_2():
  node = minimal_bst.solution([1,2,3,4,5])
  assert node.data ==3
  assert node.left.data == 1
  assert node.right.data == 4
  assert node.left.left == None
  assert node.left.right.data == 2
  assert node.right.left == None
  assert node.right.right.data == 5

def test_list_3():
  node = minimal_bst.solution([1,2,3,4,5,6,7,8])
  assert node.data == 4
  assert node.left.data == 2
  assert node.right.data == 6
  assert node.left.left.data == 1
  assert node.left.right.data == 3
  assert node.right.left.data == 5
  assert node.right.right.right.data == 8