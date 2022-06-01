import pytest 

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import fromlast

@pytest.fixture
def list():
  ll = LinkedList()
  ll.insertlast('a')
  ll.insertlast('b')
  ll.insertlast('c')
  ll.insertlast('d')
  ll.insertlast('e')
  return ll

def test_fromlast(list):
  assert fromlast.solution(list, 0).data == 'e'
  assert fromlast.solution(list, 1).data == 'd'
  assert fromlast.solution(list, 2).data == 'c'
  assert fromlast.solution(list, 3).data == 'b'
  assert fromlast.solution(list, 4).data == 'a'