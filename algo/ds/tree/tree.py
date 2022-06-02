'''
  Tree data structure
  1. Create Node class to represent a node in a tree.
  The constructor should accept an argument that gets assigned to the data property and initialize an empty array for sorting children.
  The node class should have methods 'add' and 'remove'
  2. Implement 'traverseBFS' and 'traverseDFS' on node class.
'''
class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
  
  def add(self, data):
    self.children.append(Node(data))

  def remove(self, data):
    self.children = [node for node in self.children if node.data != data]

def traverseBFS(node = Node('root')):
  traverseList = []
  tempList = [node]
  while len(tempList) > 0:
    firstNode = tempList.pop(0)
    traverseList.append(firstNode.data)
    firstNodeChildren = firstNode.children
    tempList += firstNodeChildren
  return traverseList

def traverseDFS(node = Node('root')):
  traverseList = []
  tempList = [node]
  while len(tempList) > 0:
    firstNode = tempList.pop(0)
    traverseList.append(firstNode.data)
    firstNodeChildren = firstNode.children
    tempList = firstNodeChildren + tempList

  return traverseList
