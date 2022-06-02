'''
Remove duplicated node from a linked list
'''
from algo.ds.linked_list.linkedlist import LinkedList

def solution(list = LinkedList()):
  if list.size() == 0: return
  prev = list.getfirst()
  node = prev.next
  existingData = [prev.data]
  while node != None:
    if node.data in existingData:
      prev.next = node.next
      node = node.next
    else:
      existingData.append(node.data)
      prev = prev.next
      node = node.next