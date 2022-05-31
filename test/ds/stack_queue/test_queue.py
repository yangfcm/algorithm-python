import pytest 

from algo.ds.stack_queue.queue import Queue

class TestQueue:
  def test_add(self): # Test add and its relevant methods, like peek(), size()
    q = Queue()
    q.add(1)
    assert q.size() == 1
    assert q.peek() == 1
    q.add(2)
    assert q.size() == 2
    assert q.peek() == 1
    q.add(3)
    assert q.size() == 3
    assert q.peek() == 1  # As the first element, 1 should always be at the top of queue if you peek at it.

  def test_fifo(self): # Test queue follows FIFO principles and relevant methods like remove().
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    assert q.remove() == 1
    assert q.remove() == 2
    assert q.remove() == 3

  def test_empty_queue(self):
    q = Queue()
    assert q.size() == 0
    assert q.peek() == None