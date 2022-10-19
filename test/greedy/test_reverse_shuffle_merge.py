import pytest
from algo.greedy import reverse_shuffle_merge

class TestReverseShuffleMerge:
  testData = [
    ('eggegg', 'egg'),
    ('abcdefgabcdefg', 'agfedcb'),
    ('aeiouuoiea', 'aeiou'),
    ('bdabaceadaedaaaeaecdeadababdbeaeeacacaba', 'aaaaaabaaceededecbdb')
  ]

  @pytest.mark.parametrize("str, expected", testData)
  def test_solution(self, str, expected):
    assert reverse_shuffle_merge.solution(str) == expected