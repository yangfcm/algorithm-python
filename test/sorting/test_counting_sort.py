import pytest  

from algo.sorting import counting_sort

def test_counting_sort():
  list1 = [4, 20, 1, 1, 12, 6, 24, 12, 8, 9]
  assert counting_sort.solution(list1) == [1, 1, 4, 6, 8, 9, 12, 12, 20, 24]

  list2 = [9,8,7,6,5,4,3,2,1]
  assert counting_sort.solution(list2) == [1,2,3,4,5,6,7,8,9]