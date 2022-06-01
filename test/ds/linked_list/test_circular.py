import pytest  

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import circular

@pytest.fixture
def circularList():
  ll = LinkedList()
  ll.insertlast('a')
  ll.insertlast('b')
  ll.insertlast('c')
  ll.insertlast('d')
  lastnode = ll.getlast()
  firstnode = ll.getfirst()
  lastnode.next = firstnode
  return ll

@pytest.fixture
def nonCircularList():
  ll = LinkedList()
  ll.insertlast('a')
  ll.insertlast('b')
  ll.insertlast('c')
  ll.insertlast('d')
  return ll

def test_circular_linkedlist(circularList):
  assert circular.solution(circularList) == True

def test_non_circular_linkedlist(nonCircularList):
  assert circular.solution(nonCircularList) == False