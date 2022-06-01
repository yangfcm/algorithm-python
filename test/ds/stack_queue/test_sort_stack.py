import pytest

from algo.ds.stack_queue.stack import Stack
from algo.ds.stack_queue import sort_stack

@pytest.fixture
def stackFixture():
  stack = Stack()
  stack.push(3)
  stack.push(-1)
  stack.push(0)
  stack.push(9)
  stack.push(-4)
  stack.push(2)
  return stack

def test_solution(stackFixture):
  sort_stack.solution(stackFixture)
  assert stackFixture.pop() == -4
  assert stackFixture.pop() == -1
  assert stackFixture.pop() == 0
  assert stackFixture.pop() == 2
  assert stackFixture.pop() == 3
  assert stackFixture.pop() == 9
