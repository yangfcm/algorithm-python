'''
  Add a  method to LinkedList to partition a linked list around a value x,
  such that all nodes less than x comes before all nodes greater than or equal to x.
  The partition element x can appear anywhere in the 'right partition';
  it does not need to appear between the left and right partitions.
  e.g. 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
  after partition: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''
from algo.ds.linked_list.linkedlist import LinkedList

def solution(list = LinkedList(), partition = 0):
  if list.getfirst() == None: return None
  if type(partition) != int: raise Exception('Partition out of bound.')
  partitioned = LinkedList()
  head = list.getfirst()
  while head != None:
    if head.data < partition:
      partitioned.insertfirst(head.data)
    else:
      partitioned.insertlast(head.data)
    head = head.next

  return partitioned