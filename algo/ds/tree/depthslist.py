'''
  Given a binary tree, create a list of all the nodes at each level.
  If you have a tree with N levels, you'll have N lists.
  Example:
        0
      /   \
      1     3
    / \   /
    4  6  5
  Answer: [[Node(0)], [Node(1), Node(3)], [Node(4), Node(6), Node(5)]]
'''
from algo.ds.tree.bst import Node

def solution(tree = Node('root')):
  lists = []
  current = []  # List of nodes for the current level
  if tree != None:
    current.append(tree)
  while len(current) > 0: # If there's no node in current, it means the end of tree traversal.
    lists.append(current)
    parents = current # remember the current level
    current = [] # Move to the next level
    for p in parents:
      if p.left != None:
        current.append(p.left)
      if p.right != None:
        current.append(p.right)
  return lists