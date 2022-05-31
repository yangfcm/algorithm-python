import pytest

from algo.ds.stack_queue import get_min
from algo.ds.stack_queue.stack import Stack

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
  min = get_min.solution(stackFixture)
  assert min == -4
  assert stackFixture.size() == 6 # Assert the stack is intact.