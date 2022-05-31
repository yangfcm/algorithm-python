import pytest

from algo.ds.stack_queue.animal_queue import AnimalQueue, Animal, AnimalSpecies


@pytest.fixture
def animalQueue():
  animalQueue = AnimalQueue()
  animalQueue.enqueue(AnimalSpecies.CAT)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.CAT)
  return animalQueue

def test_dequeue(animalQueue):
  assert animalQueue.dequeue() == Animal(AnimalSpecies.CAT, 0)
  assert animalQueue.dequeue() == Animal(AnimalSpecies.DOG, 1)
  assert animalQueue.dequeue() == Animal(AnimalSpecies.DOG, 2)
  assert animalQueue.dequeue() == Animal(AnimalSpecies.CAT, 3)
  assert animalQueue.dequeue() == None

def test_dequeue_cat(animalQueue):
  assert animalQueue.dequeueCat() == Animal(AnimalSpecies.CAT, 0)
  assert animalQueue.dequeueCat() == Animal(AnimalSpecies.CAT, 3)
  assert animalQueue.dequeueCat() == None

def test_dequeue_dog(animalQueue):
  assert animalQueue.dequeueDog() == Animal(AnimalSpecies.DOG, 1)
  assert animalQueue.dequeueDog() == Animal(AnimalSpecies.DOG, 2)
  assert animalQueue.dequeueDog() == None