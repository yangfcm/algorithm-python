'''
  Say you have an array for which the i-th element is the price of a given stock on day i.
  Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
  Example [7, 1, 5, 3, 6, 4] => 7 ((5-1) + (6-3) = 7)
    The array indicates the stock price for each day:
    +-----------------------------+
    + D1 | D2 | D3 | D4 | D5 | D6 +
    +-----------------------------+
    +  7 |  1 |  5 |  3 |  6 |  4 +
    +-----------------------------+
  To gain the max profit, you need to buy stock  at price of 1 on D2 and sell it at price of 5 on D3. You earn 5 - 1 = 4 in this transaction.
  Then you buy stock at price of 3 on D4 and sell it at price of 6 on D5. You earn 6 - 3 = 3 in this transaction.
  So in total, the maximum profit you can earn is 4 + 3 = 7.
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