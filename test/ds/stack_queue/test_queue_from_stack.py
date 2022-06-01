import pytest 

from algo.ds.stack_queue.queue_from_stack import QueueFromStack

class TestQueueFromStack:
  def test_add(self): # Test add() and peek() method
    qfs = QueueFromStack()
    qfs.add(1)
    assert qfs.peek() == 1
    assert qfs.size() == 1
    qfs.add(2)
    assert qfs.peek() == 1
    assert qfs.size() == 2
    qfs.add(3)
    assert qfs.peek() == 1
    assert qfs.size() == 3

  def test_fifo(self): # Test queue follows FIFO principles
    qfs = QueueFromStack()
    qfs.add(1)
    qfs.add(2)
    qfs.add(3)
    assert qfs.remove() == 1
    assert qfs.remove() == 2
    assert qfs.remove() == 3
