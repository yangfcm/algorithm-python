import pytest  

from algo.ds.stack_queue import weave
from algo.ds.stack_queue.queue import Queue

@pytest.fixture
def queue1():
  q1 = Queue()
  q1.add(1)
  q1.add(2)
  q1.add(3)
  return q1

@pytest.fixture
def queue2():
  q2 = Queue()
  q2.add('one')
  q2.add('two')
  q2.add('three')
  q2.add('four')
  return q2

def test_solution_1(queue1, queue2):
  weaved = weave.solution(queue1, queue2)
  assert weaved.remove() == 1
  assert weaved.remove() == 'one'
  assert weaved.remove() == 2
  assert weaved.remove() == 'two'
  assert weaved.remove() == 3
  assert weaved.remove() == 'three'
  assert weaved.remove() == 'four'

def test_solution_2(queue2, queue1):
  weaved = weave.solution(queue2, queue1)
  assert weaved.remove() == 'one'
  assert weaved.remove() == 1
  assert weaved.remove() == 'two'
  assert weaved.remove() == 2
  assert weaved.remove() == 'three'
  assert weaved.remove() == 3
  assert weaved.remove() == 'four'
