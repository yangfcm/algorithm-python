import pytest

from algo.ds.stack_queue.animal_queue import AnimalQueue, AnimalSpecies

animalQueue = AnimalQueue()

@pytest.fixture(autouse=True)
def run_around_tests():
  animalQueue.enqueue(AnimalSpecies.CAT)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.CAT)
  animalQueue.enqueue(AnimalSpecies.CAT)
  animalQueue.enqueue(AnimalSpecies.DOG)
  yield

def test_dequeue():
  pass

def test2():
  pass