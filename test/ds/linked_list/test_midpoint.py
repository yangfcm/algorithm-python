import pytest

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import midpoint

@pytest.fixture
def listFixture():
  list = LinkedList()
  list.insertlast(1)
  list.insertlast(2)
  list.insertlast(3)
  list.insertlast(4)
  list.insertlast(5)
  list.insertlast(6)
  return list

def test_solution(listFixture):
  assert midpoint.solution(listFixture).data == 3

def test_solution(listFixture):
  listFixture.insertlast(7)
  assert midpoint.solution(listFixture).data == 4