'''
  Implement three ways to traverse a b-tree: inorder, preorder and postorder.
'''

def preorderTraverse(node):
  traverseList = []

  def doTraverse(node):
    if node==None: return
    traverseList.append(node.data)
    doTraverse(node.left)
    doTraverse(node.right)
  
  doTraverse(node)
  return traverseList
  

def inorderTraverse(node):
  traverseList = []

  def doTraverse(node):
    if node==None: return
    doTraverse(node.left)
    traverseList.append(node.data)
    doTraverse(node.right)
  
  doTraverse(node)
  return traverseList


def postorderTraverse(node):
  traverseList = []

  def doTraverse(node):
    if node==None: return
    doTraverse(node.left)
    doTraverse(node.right)
    traverseList.append(node.data)
  
  doTraverse(node)
  return traverseList