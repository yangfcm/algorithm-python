'''
 An animal queue, which holds only dogs and cats, operates on a strictly "fist in, first out" basis.
 People must adopt either the first of all animals at the shelter,
 or they can select whether they would prefer the first dog or the first cat(cannot select a specific animal they like)
 Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
'''
from collections import deque
from enum import Enum

class AnimalSpecies(Enum):
  DOG = 1
  CAT = 2

class Animal:
  def __init__(self, animal, order):
    self.animal = animal
    self.order = order

class AnimalQueue:
  def __init__(self):
    self.order = 0
    self.dogQueue = deque()
    self.catQueue = deque()
  
  # Add an animal, either cat or dog into the queue.
  def enqueue(self, animal):
    if animal == AnimalSpecies.DOG:
      self.dogQueue.append(animal)
      self.order += 1
    elif animal == AnimalSpecies.CAT:
      self.catQueue.append(animal)
      self.order += 1
    else:
      raise Exception('Not dog or cat')

  def dequeueDog(self):
    if len(self.dogQueue) == 0:
      return None
    return self.dogQueue.popleft()

  def dequeueCat(self):
    if len(self.catQueue) == 0:
      return None
    return self.catQueue.popleft()

  def dequeue(self):
    firstCat = self.catQueue[0] if len(self.catQueue) > 0 else None
    firstDog = self.dogQueue[0] if len(self.dogQueue) > 0 else None

    if firstCat is None and firstDog is None: return None
    if not firstCat is None and firstDog is None: return self.dequeueCat()
    if firstCat is None and not firstDog is None: return self.dequeueDog()
    if not firstCat is None and not firstDog is None:
      return self.dequeueCat() if firstCat.order < firstDog.order else self.dequeueDog()
    return None

