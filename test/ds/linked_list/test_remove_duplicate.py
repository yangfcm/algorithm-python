import pytest 

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import remove_duplicate

@pytest.fixture
def listFixture():
  list = LinkedList()
  list.insertlast("a")
  list.insertlast("b")
  list.insertlast("b")
  list.insertlast("b")
  list.insertlast("c")
  list.insertlast("c")
  list.insertlast("d")
  list.insertlast("d")
  list.insertlast("d")
  list.insertlast("d")
  list.insertlast("b")
  list.insertlast("c")
  return list

def test_solution(listFixture):
  assert listFixture.size() == 12
  remove_duplicate.solution(listFixture)
  assert listFixture.size() == 4
  assert listFixture.get(0).data == 'a'
  assert listFixture.get(1).data == 'b'
  assert listFixture.get(2).data == 'c'
  assert listFixture.get(3).data == 'd'