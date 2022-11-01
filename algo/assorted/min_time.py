'''
  Minimum Time Required: You are planning production for an order.
  You have a number of machines that each have a fixed number of days to produce an item.
  Given that all the machines operate simultaneously,
  determine the minimum number of days to produce the required order.

  Example: machines = [2, 3, 2], goal = 10 -> 8
  There are three machines, and machine 1 and 3 needs to spend 2 days to produce one item;
  machine 2 spend 3 days to product one item.
  The schedule is as below:
  Day | Production | Finished items
  ---------------------------------
  1   | 0          | 0
  2   | 2          | 2
  3   | 1          | 3
  4   | 2          | 5
  5   | 0          | 5
  6   | 3          | 8
  7   | 0          | 8
  8   | 2          | 10
  So on day 8, we can produce 10 items which reaches the goal.
'''
from math import ceil, floor


def solution(machines, goal):
  minDays = floor(goal * min(machines) / len(machines))
  maxDays = ceil(goal * max(machines) / len(machines))
  days = max(minDays, maxDays)
  while True:
    mid = (minDays + maxDays) // 2
    if minDays == mid or maxDays == mid: break
    if production_so_far(machines, mid) < goal:
      minDays = mid
    else:
      maxDays = mid
    days = max(minDays, maxDays)
  return days

# Work out how many items are produced accumulatively by the end of k-th day with the given machines
def production_so_far(machines, k):
  items = 0
  for m in machines:
    items += k//m
  return items
