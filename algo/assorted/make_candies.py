'''
  Make Candies: A candy factory wants to make n candies. To make candies, it needs machines and workers.
  The factory starts with m machines and w workers. With that, it can make m w candies each day.
  By the end of day, the factory can decide whether to spend some of his candies to buy more machines or hire more workers.
  Buying a machine or hiring a worker costs p units, and there is no limit to the number of machines or workers it can have.
  The factory wants to minimize the number of days to produce the required number of candies at the end of a day.
  Write a function to determine that number of days.

  Example: m = 3, w = 1, p = 2, n = 12 -> 3
  Day 1: production = m * w = 3 * 1 = 3.
  By the end of Day 1, factory can spend p = 2 of the production to hire another worker, so now w = 2 and net production is 3 - 2 = 1
  Day 2: production = m * w + net production of day 1 = 3 * 2 + 1 = 7.
  By the end of Day 2, factory can spend 3 (p = 2) of the production to buy new machines or hire new workers.
  Let's use 1 to buy new machine and 2 to hire new workers, so now m = 4, w = 4, and the net production is 7 - 3*2 = 1.
  Day 3: production = 4 * 4 = 16 > 12. So it needs 3 days to reach the target production.
'''
from math import ceil, inf

def solution(m, w, p, n):
  if n <= p: return ceil(n / (m * w))
  days, invest, production, netProduction = 0, 0, 0, 0
  ans = inf
  while True:
    ans = min(ans, days + ceil((n - production) / (m * w))) # Consider the case if we continue producing with the current machines and workers.
    days += 1
    (m, w) = max_production(m, w, invest)
    production = m * w + netProduction
    invest = production // p  # Take as much as possible from production to increase the productivity.
    netProduction = production - invest * p
    if production >= n: break

  return min(ans, days)

# Given the available machines and workers and total invest, work out how to 
# allocate invest between machines and workers so that daily productivity can achieve the maximum.
# Return the new machines and workers after invested.
def max_production(m, w, invest = 0):
  total = m + w + invest
  half = total // 2
  if m > w:
    m = max(m, half)
    w = total - m
  else:
    w = max(w, half)
    m = total - w
  return (m, w)

