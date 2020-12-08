'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
e.g. [7, 1, 5, 3, 6, 4] => 7 ( (5-1) + (6-3) = 7 )
'''
def solution(prices):
  profit, buyPrice, sellPrice, holding = 0, 0, 0, False
  prices.append(0)
  for i in range(len(prices)-1):
    if prices[i] <= prices[i+1] and not holding:
      # Buy stock
      buyPrice = prices[i]
      holding = True
    if prices[i] > prices[i+1] and holding:
      # Sell stock and calculate the profit. Consider when iteration hits the last element
      sellPrice = prices[i]
      holding = False
      profit += (sellPrice - buyPrice)
      buyPrice, sellPrice = 0, 0
  return profit