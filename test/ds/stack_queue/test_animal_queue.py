import pytest

from algo.ds.stack_queue.animal_queue import AnimalQueue, AnimalSpecies


@pytest.fixture
def animalQueue():
  animalQueue = AnimalQueue()
  animalQueue.enqueue(AnimalSpecies.CAT)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.DOG)
  animalQueue.enqueue(AnimalSpecies.CAT)
  return animalQueue

def test_dequeue(animalQueue):
  animal = animalQueue.dequeue()
  assert animal.animal == AnimalSpecies.CAT
  assert animal.order == 0

  print(animalQueue.order)
  animal = animalQueue.dequeue()
  assert animal.animal == AnimalSpecies.DOG
  assert animal.order == 1
  
  animal = animalQueue.dequeue()
  assert animal.animal == AnimalSpecies.DOG
  assert animal.order == 2
  
  animal = animalQueue.dequeue()
  assert animal.animal == AnimalSpecies.CAT
  assert animal.order == 3

  animal = animalQueue.dequeue()
  assert animal == None

def test_dequeue_cat(animalQueue):
  cat = animalQueue.dequeueCat()
  assert cat.animal == AnimalSpecies.CAT
  assert cat.order == 0

  cat = animalQueue.dequeueCat()
  assert cat.animal == AnimalSpecies.CAT
  assert cat.order == 3

  cat = animalQueue.dequeueCat()
  assert cat == None

def test_dequeue_dog(animalQueue):
  dog = animalQueue.dequeueDog()
  assert dog.animal == AnimalSpecies.DOG
  assert dog.order == 1

  dog = animalQueue.dequeueDog()
  assert dog.animal == AnimalSpecies.DOG
  assert dog.order == 2

  dog = animalQueue.dequeueDog()
  assert dog == None