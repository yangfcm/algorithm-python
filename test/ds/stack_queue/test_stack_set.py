import pytest
from algo.ds.stack_queue.stack_set import StackSet

class TestStackSet:
  def populateData(self):
    ss = StackSet(3)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    ss.push(7)
    return ss

  def test_push(self):
    ss = StackSet(3)
    assert ss.size() == 0
    assert ss.peek() == None
    ss.push(1)
    assert ss.size() == 1
    assert ss.peek() == 1
    ss.push(2)
    assert ss.size() == 1
    assert ss.peek() == 2
    ss.push(3)
    assert ss.size() == 1
    assert ss.peek() == 3
    ss.push(4)
    assert ss.size() == 2
    assert ss.peek() == 4
    ss.push(5)
    assert ss.size() == 2
    assert ss.peek() == 5
    ss.push(6)
    assert ss.size() == 2
    assert ss.peek() == 6
    ss.push(7)
    assert ss.size() == 3
    assert ss.peek() == 7

  def test_lifo(self):
    ss = StackSet(3)
    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(6)
    ss.push(7)
    assert ss.pop() == 7
    assert ss.size() == 2
    assert ss.pop() == 6
    assert ss.size() == 2
    assert ss.pop() == 5
    assert ss.size() == 2
    assert ss.pop() == 4
    assert ss.size() == 1
    assert ss.pop() == 3
    assert ss.size() == 1
    assert ss.pop() == 2
    assert ss.size() == 1
    assert ss.pop() == 1
    assert ss.size() == 0

  def test_peekat(self):
    ss = self.populateData()
    assert ss.peekat(0) == 3
    assert ss.peekat(1) == 6
    assert ss.peekat(2) == 7
    assert ss.peekat(3) == None
  
  def test_popat(self):
    ss = self.populateData()
    assert ss.popat(0) == 3
    assert ss.size() == 3
    assert ss.popat(0) == 2
    assert ss.size() == 3
    assert ss.popat(0) == 1
    assert ss.size() == 2
    assert ss.popat(0) == 6
    assert ss.size() == 2