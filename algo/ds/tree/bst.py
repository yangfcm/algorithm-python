'''
  Binary Search Tree
  1. Implement the Node class to create a binary search tree.
  The constructor should initialize values 'data', 'left' and 'right'
  2. Implement the 'insert' method for the Node class.
  Insert should accept an argument 'data', then create a new node and insert it at the appropriate location in the tree.
  By 'appropriate', the new node should follow the rule of BST that is for any node in BST, the left child should be less than the node and the right child should be bigger than the node.
  3. Implement the 'contain' method for the Node class.
  Contain should accept a 'data' argument and return the Node in the tree with the same value
  If the value isn't in the tree, return None.
'''
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, data):
    if data < self.data:
      if self.left == None:
        self.left = Node(data)
      else:
        self.left.insert(data)
    if data > self.data:
      if self.right == None:
        self.right = Node(data)
      else:
        self.right.insert(data)

  def contain(self, data):
    if self.data == data: return self
    if data < self.data and self.left != None:
      return self.left.contain(data)
    if data > self.data and self.right != None:
      return self.right.contain(data)

    return None