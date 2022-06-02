import pytest 

from algo.ds.linked_list.linkedlist import LinkedList
from algo.ds.linked_list import sumlists

@pytest.fixture
def list1():
  list = LinkedList()
  list.insertlast(7)
  list.insertlast(1)
  list.insertlast(6)
  return list

@pytest.fixture
def list2():
  list = LinkedList()
  list.insertlast(5)
  list.insertlast(9)
  list.insertlast(2)
  return list

def test_solution_case1(list1, list2):
  sum = sumlists.solution(list1, list2)
  assert sum.get(0).data == 2
  assert sum.get(1).data == 1
  assert sum.get(2).data == 9

@pytest.fixture
def list3():
  list = LinkedList()
  list.insertlast(9)
  list.insertlast(9)
  list.insertlast(9)
  list.insertlast(9)
  return list

@pytest.fixture
def list4():
  list = LinkedList()
  list.insertlast(1)
  return list

def test_solution_case1(list3, list4):
  sum = sumlists.solution(list3, list4)
  assert sum.get(0).data == 0
  assert sum.get(1).data == 0
  assert sum.get(2).data == 0
  assert sum.get(3).data == 0
  assert sum.get(4).data == 1

@pytest.fixture
def list5():
  list = LinkedList()
  list.insertlast(9)
  list.insertlast(9)
  list.insertlast(9)
  return list

@pytest.fixture
def list6():
  list = LinkedList()
  list.insertlast(9)
  list.insertlast(8)
  return list

def test_solution_case1(list5, list6):
  sum = sumlists.solution(list5, list6)
  assert sum.get(0).data == 8
  assert sum.get(1).data == 8
  assert sum.get(2).data == 0
  assert sum.get(3).data == 1