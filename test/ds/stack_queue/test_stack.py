from turtle import st
import pytest

from algo.ds.stack_queue.stack import Stack

class TestStack:
  def test_push(self): # Test push and its relevant methods, like peek(), size()
    s = Stack()
    s.push(1)
    assert s.size() == 1
    assert s.peek() == 1
    s.push(2)
    assert s.size() == 2
    assert s.peek() == 2
    s.push(3)
    assert s.size() == 3
    assert s.peek() == 3

  def test_fifo(self):  # Test stack follows FIFO principles and relevant methods, like pop()
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

  def test_empty_stack(self):
    s = Stack()
    assert s.size() == 0
    assert s.peek() == None