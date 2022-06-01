'''
  Weave: Receive two queues as arguments and combines the contents of each into a new, third queue.
  The new queue should contain the alterating of the two queues.
  The function should handle queues of different lengths without inserting 'undefined' into the new one
  DO NOT access the array inside of any queue, only use 'add', 'remove' and 'peek' methods
  Example:
    queueOne = Queue();
    queueOne.add(1);
    queueOne.add(2);
    queueTwo = Queue();
    queueTwo.add('Hi');
    queueTwo.add('There');
    q = weave(queueOne, queueTwo);
    q.remove()  // 1
    q.remove()  // 'Hi'
    q.remove()  // 2
    q.remove() // 'There'
'''
from algo.ds.stack_queue.queue import Queue

def solution(q1, q2):
  q = Queue()
  while q1.peek() != None or q2.peek() != None:
    if q1.peek() != None:
      q.add(q1.remove())
    if q2.peek() != None:
      q.add(q2.remove())
  return q