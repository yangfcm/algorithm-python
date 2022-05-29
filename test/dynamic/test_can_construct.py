from algo.dynamic import can_construct

class TestCanConstruct:
  
  def test_solution1(self):
    assert can_construct.solution1("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct.solution1("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == True
    assert can_construct.solution1("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == False

  def test_solution2(self):
    assert can_construct.solution2("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct.solution2("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == True
    assert can_construct.solution2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == False
    assert can_construct.solution2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == False

  def test_solution3(self):
    assert can_construct.solution3("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct.solution3("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == True
    assert can_construct.solution3("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == False
    assert can_construct.solution3("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
      "e",
      "ee",
      "eee",
      "eeee",
      "eeeee",
      "eeeeee",
    ]) == False