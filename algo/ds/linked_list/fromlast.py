'''
  Given a linked list and integer n, return the element n spaces from the last node in the list.
  Example
    list = new LinkedList();
    list.insertlast('a');
    list.insertlast('b');
    list.insertlast('c');
    list.insertlast('d');
    fromLast(list, 2).data;   // 'b'
'''
from algo.ds.linked_list.linkedlist import LinkedList

def solution(list = LinkedList(), n = 0):
  if n < 0 or n >= list.size(): raise Exception('Out of bound')
  slow = list.getfirst()
  fast = list.getfirst()
  while n > 0:
    fast = fast.next
    n -= 1
  while fast.next != None:
    slow = slow.next
    fast = fast.next
  return slow