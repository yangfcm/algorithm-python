'''
  Given a sorted, increasing order list with unique integer elements,
  write a function to create a binary search tree with minimal height.
  Note: A minimal bst has about the same number of nodes on the left of each node as on the right.
'''
  # e.g. [1,2,3,4,5,6, 7] =>
  #      4
  #    /   \
  #   2     6
  #  / \   / \
  # 1  3  5  7

'''
Solution: The middle of each subsection of the list becomes the root of the node.
The left half of the list will become the left subtree and the right half of the list will become the right subtree.
'''
from algo.ds.tree.bst import Node

def solution(list):
  return createBSTHelper(list, 0, len(list) - 1)

def createBSTHelper(list, start, end):
  if end < start: return None
  mid = (start + end) // 2
  n = Node(list[mid])
  n.left = createBSTHelper(list, start, mid-1)
  n.right = createBSTHelper(list, mid+1, end)
  return n