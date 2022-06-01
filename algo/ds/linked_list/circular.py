'''
  Given a linked list, return true if it is circular, false if it is not.
  Example:
    l = new LinkedList();
    a = new Node('a');
    b = new Node('b');
    c = new Node('c');
    l.head = a;
    a.next = b;
    b.next = c;
    c.next = b;  # The last node's next object points at the first node.
    circular(l) // true
'''
from algo.ds.linked_list.linkedlist import LinkedList

def solution(list = LinkedList()):
  slow = list.getfirst()
  fast = list.getfirst()

  while not fast.next is None and not fast.next.next is None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  
  return False