'''
  Swap Nodes: https://www.hackerrank.com/challenges/swap-nodes-algo/problem
'''
from algo.ds.tree.bst import Node
from algo.ds.tree import depthslist
from algo.ds.tree.btree_traverse import inorderTraverse

'''
   Given a 2D array (indexes), return a tree root node that is represented by the array.
   Its root node is always 1 and its leaf nodes are natural numbers: 2, 3, 4, 5 ... -1 means no node for this position.
   Example: indexes = [
      [2, 3],
      [4, -1],
      [5, -1],
      [6, -1],
      [7, 8],
      [-1, 9],
      [-1, -1],
      [10, 11],
      [-1, -1],
      [-1, -1],
      [-1, -1],
    ]
    Its corresponding tree should look like:
            1
           / \
          2   3
         /   /
        4    5
       /    /\
      6    7  8
       \      /\
        9    10 11 
'''
def build_tree(indexes):
  nodeIndexes = []
  nodesMap = {
    1: Node(1)
  }
  for idx in indexes:
    left, right = None, None
    if idx[0] != -1: 
      left = Node(idx[0])
      nodesMap[left.data] = left
    if idx[1] != -1: 
      right = Node(idx[1])
      nodesMap[right.data] = right
    nodeIndexes.append([left, right])
  
  for i in range(len(nodeIndexes)):
    nodesMap[i + 1].left = nodeIndexes[i][0]
    nodesMap[i + 1].right = nodeIndexes[i][1]

  return nodesMap[1]

def solution(indexes, queries):
  traversalResult = []
  tree = build_tree(indexes)  # Create B-Tree from indexes
  levelsList = depthslist.solution(tree)  # Work out the elements for each level of the B-Tree
  depths = len(levelsList)
  for q in queries:
    k = 1
    level = k*q
    while level <= depths:  # Do swap for each node at the level.
      levelNodes = levelsList[level - 1]
      for node in levelNodes:
        node.left, node.right = node.right, node.left
      k += 1
      level = k*q
    traversalResult.append(inorderTraverse(tree))

  return traversalResult