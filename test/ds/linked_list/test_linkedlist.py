import pytest 

from algo.ds.linked_list.linkedlist import LinkedList

class TestLinkedList:
  def populate_data(self):
    ll = LinkedList()
    ll.insertlast(1)
    ll.insertlast(2)
    ll.insertlast(3)
    ll.insertlast(4)
    ll.insertlast(5)
    return ll

  def test_init_linkedlist(self):
    ll = LinkedList()
    assert ll.size() == 0
    assert ll.getfirst() == None
    assert ll.getlast() == None

  def test_get_method(self):
    ll = self.populate_data()
    assert ll.getfirst().data == 1
    assert ll.getlast().data == 5
    assert ll.get(0).data == 1
    assert ll.get(1).data == 2
    assert ll.get(2).data == 3
    assert ll.get(3).data == 4
    assert ll.get(4).data == 5

  def test_insert_method(self):
    ll = LinkedList()
    ll.insertlast(1)
    assert ll.get(0).data == 1
    ll.insertlast(2)
    assert ll.get(1).data == 2
    ll.insertfirst(0)
    assert ll.get(0).data == 0

    ll.insert(99, 1)
    assert ll.get(0).data == 0
    assert ll.get(1).data == 99
    assert ll.get(2).data == 1
    assert ll.get(3).data == 2

  def test_remove_method(self):
    ll = self.populate_data()
    ll.removefirst()
    assert ll.size() == 4
    assert ll.getfirst().data == 2

    ll.removelast()
    assert ll.size() == 3
    assert ll.getlast().data == 4

    ll.remove(1)
    assert ll.size() == 2
    assert ll.get(0).data == 2
    assert ll.get(1).data == 4