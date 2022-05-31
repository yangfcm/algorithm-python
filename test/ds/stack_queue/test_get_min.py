import pytest

from collections import deque
from algo.ds.stack_queue import get_min

def test_solution_case1():
  stack = deque([2, 5, 3, 0, -4, -1, 9, 1])
  min = get_min.solution(stack)
  assert min == -4
  assert len(stack) == 8  # Assert the stack is intact.
