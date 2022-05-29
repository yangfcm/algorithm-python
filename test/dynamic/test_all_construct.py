from algo.dynamic import all_construct

class TestAllConstruct:

  def test_solution1(self):
    assert all_construct.solution1("purple", ["purp", "p", "ur", "le", "purpl"]) == \
     [["purp", "le"], ["p", "ur", "p", "le"]]
    assert all_construct.solution1("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == \
      [
        ["ab", "cd", "ef"],
        ["ab", "c", "def"],
        ["abc", "def"],
        ["abcd", "ef"],
      ]