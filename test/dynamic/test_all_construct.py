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

  def test_solution2(self):
    assert all_construct.solution2("purple", ["purp", "p", "ur", "le", "purpl"]) == \
     [["purp", "le"], ["p", "ur", "p", "le"]]
    assert all_construct.solution2("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == \
      [
        ["ab", "cd", "ef"],
        ["ab", "c", "def"],
        ["abc", "def"],
        ["abcd", "ef"],
      ]
    assert all_construct.solution2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == []

    def test_solution3(self):
      assert all_construct.solution3("purple", ["purp", "p", "ur", "le", "purpl"]) == \
      [["purp", "le"], ["p", "ur", "p", "le"]]
      assert all_construct.solution3("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == \
        [
          ["ab", "cd", "ef"],
          ["ab", "c", "def"],
          ["abc", "def"],
          ["abcd", "ef"],
        ]
      assert all_construct.solution3("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == []