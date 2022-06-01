import pytest
from algo.ds.stack_queue.stack_set import StackSet

class TestStackSet:
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