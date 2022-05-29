from algo.dynamic import count_construct

class TestCountConstruct:

  def test_solution1(self):
    assert count_construct.solution1("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0
    assert count_construct.solution1("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert count_construct.solution1("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    assert count_construct.solution1("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == 4
  
  def test_solution2(self):
    assert count_construct.solution2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0
    assert count_construct.solution2("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert count_construct.solution2("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    assert count_construct.solution2("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == 4
    assert count_construct.solution2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == 0
  
  def test_solution3(self):
    assert count_construct.solution3("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0
    assert count_construct.solution3("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert count_construct.solution3("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    assert count_construct.solution3("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == 4
    assert count_construct.solution3("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == 0