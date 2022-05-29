from algo.dynamic import count_construct

class TestCountConstruct:

  def test_solution1(self):
    assert count_construct.solution1("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0
    assert count_construct.solution1("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert count_construct.solution1("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    assert count_construct.solution1("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) == 4