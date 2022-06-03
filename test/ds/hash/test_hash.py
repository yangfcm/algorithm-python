import pytest  

from algo.ds.hash.hash import HashTable

class TestHashTable:
  def test_init(self):
    t = HashTable()
    assert t.count == 0
    assert t.size == 8

    t = HashTable(10) # Specify my own size.
    assert t.size == 10

  def test_put_get(self):
    t = HashTable()
    assert t.put('name', 'John') == 'John'
    assert t.put('age', 12) == 12
    assert t.put('hobbies', ['cooking', 'fishing', 'camping']) == ['cooking', 'fishing', 'camping']
    assert t.put('age', 32) == 32 # Test can override a key.

    assert t.get('name') == 'John'
    assert t.get('age') == 32
    assert t.get('hobbies') == ['cooking', 'fishing', 'camping']
    assert t.get('unknown_key') == None

  def test_remove(self):
    t = HashTable()
    t.put('a', 1)
    t.put('b', 2)
    t.put('c', 3)
    assert t.remove('a') == 1
    assert t.remove('b') == 2
    assert t.get('a') == None
    assert t.get('b') == None
    assert t.remove('b') == None
    assert t.remove('d') == None

  def test_resize_expansion(self):
    t = HashTable(2)
    t.put('a', 1)
    assert t.size == 2
    t.put('b', 2) # Now resize to 4.
    assert t.size == 4
    t.put('c', 3)
    assert t.get('a') == 1
    assert t.get('b') == 2
    assert t.get('c') == 3

    t.remove('a')
    t.remove('b')
    print(t.count)
    assert t.size == 4
    t.remove('c') # Now resize to 2.
    assert t.size == 2