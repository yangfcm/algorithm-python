'''
 An animal queue, which holds only dogs and cats, operates on a strictly "fist in, first out" basis.
 People must adopt either the first of all animals at the shelter,
 or they can select whether they would prefer the first dog or the first cat(cannot select a specific animal they like)
 Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
'''
from algo.ds.stack_queue.queue import Queue
from enum import Enum

class AnimalSpecies(Enum):
  DOG = 1
  CAT = 2

class Animal:
  def __init__(self, animal, order):
    self.animal = animal
    self.order = order
  
  def __eq__(self, other):
    if(self is None and other is None): return True
    elif(self is None or other is None): return False
    else: return self.__dict__ == other.__dict__ 

class AnimalQueue:
  def __init__(self):
    self.order = 0
    self.dogQueue = Queue()
    self.catQueue = Queue()
  
  # Add an animal, either cat or dog into the queue.
  def enqueue(self, animal):
    if animal == AnimalSpecies.DOG:
      self.dogQueue.add(Animal(AnimalSpecies.DOG, self.order))
      self.order += 1
    elif animal == AnimalSpecies.CAT:
      self.catQueue.add(Animal(AnimalSpecies.CAT, self.order))
      self.order += 1
    else:
      raise Exception('Not dog or cat')

  def dequeueDog(self):
    if self.dogQueue.isempty():
      return None
    return self.dogQueue.remove()

  def dequeueCat(self):
    if self.catQueue.isempty():
      return None
    return self.catQueue.remove()

  def dequeue(self):
    firstCat = self.catQueue.peek() if self.catQueue.size() > 0 else None
    firstDog = self.dogQueue.peek() if self.dogQueue.size() > 0 else None

    if firstCat is None and firstDog is None: return None
    if not firstCat is None and firstDog is None: return self.dequeueCat()
    if firstCat is None and not firstDog is None: return self.dequeueDog()
    if not firstCat is None and not firstDog is None:
      return self.dequeueCat() if firstCat.order < firstDog.order else self.dequeueDog()
    return None

