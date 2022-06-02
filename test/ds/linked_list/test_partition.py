import pytest 

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import partition

@pytest.fixture 
def listFixture():
  list = LinkedList()
  list.insertlast(10)
  list.insertlast(3)
  list.insertlast(8)
  list.insertlast(6)
  list.insertlast(7)
  list.insertlast(1)
  list.insertlast(9)
  list.insertlast(2)
  return list

def test_solution(listFixture):
  partitioned = partition.solution(listFixture, 5)
  assert partitioned.get(0).data < 5
  assert partitioned.get(1).data < 5
  assert partitioned.get(2).data < 5
  assert partitioned.get(3).data > 5
  assert partitioned.get(4).data > 5
  assert partitioned.get(5).data > 5
  assert partitioned.get(6).data > 5
  assert partitioned.get(7).data > 5

