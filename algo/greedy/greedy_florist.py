'''
  Greedy Florist:  A group of friends want to buy a bouquet of flowers. The florist wants to maximize the earning.
  To do this, he multiplies the price of each flower by the number of the same customer's previously purchased flowers plus 1.
  For example, if a customer buys one flower previously, then he will be charged (1+1)*original price for his next flower.
  Given the number of friends and an array of the original prices of the flowers, work out the minimum cost to buy all of the flowers.

  Example: costs = [1, 3, 5, 7, 9] k = 3 -> 29
  The original prices of flowers are 1, 3, 5, 7, 9 and we have 3 people(p1, p2, p3) to buy all of the 5 flowers.
  To spend the least money, p1, p2 and p3 buy the three most expensive flowers (5, 7, 9) respectively,
  Then two of the three people should buy their second flowers at price of 1 and 3, which will cost them (1+1)*1 = 2 and (1+1)*3 = 6 respectively.
  So the minimum cost is 5 + 7 + 9 + 2 + 6 = 29
'''
def solution(costs, k):
  costs.sort()
  sorted = costs[::-1]  # Sort the costs array from biggest to smallest

  totalCost = 0
  for i, cost in enumerate(sorted):
    totalCost += cost * (1 + i//k)

  return totalCost