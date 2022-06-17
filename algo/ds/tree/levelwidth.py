'''
  Given the root node of a tree, return an array to show the width of each level.
  Example:
    Given:
        0
      / |  \
    1   2   3
    |       |
    4       5
    Answer: [1, 3, 2]
'''
from algo.ds.tree.tree import Node

def solution(tree = Node('root')):
  widths = [0]
  list = [tree, 's']  # 's' is a stop sign to indicate the end of a level.

  while len(list) > 1: # If 'list' has only one element ('s') left, it means the traversal of tree is finished
    node = list.pop(0)
    if node == 's': # If the node returned is 's', it means it reaches the end of a level.
      widths.append(0)
      list.append('s')
    else:
      list.extend(node.children)
      widths[len(widths) - 1] += 1
  return widths