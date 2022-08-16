import pytest

from algo.sorting import count_inversions

def test_count_inverions():
  list1 = [1, 1, 1, 2, 2, 3, 4, 4, 5]
  list2 = [2, 1, 3, 1, 2]
  list3 = [5, 4, 4, 3, 2, 2, 1, 0]

  assert count_inversions.solution1(list1) == 0
  assert count_inversions.solution1(list2) == 4
  assert count_inversions.solution1(list3) == 26
  
  assert count_inversions.solution2(list1) == 0
  assert count_inversions.solution2(list2) == 4
  assert count_inversions.solution2(list3) == 26