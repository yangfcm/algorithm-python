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