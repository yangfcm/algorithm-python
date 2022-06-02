'''
 Given a node (binary tree), validate if it's a binary search tree.
'''
def solution(node, min = None, max = None):
  if max != None and node.data > max:
    return False
  if min != None and node.data < min:
    return False
  
  if node.left != None and not solution(node.left, min, node.data):
    return False
  if node.right != None and not solution(node.right, node.data, max):
    return False
  
  return True