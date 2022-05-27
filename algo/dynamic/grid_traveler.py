'''
  Say that you are a traveler on a 2D grid.
  You begin in the top-left corner and end in the bottom-right corner.
  You may only move down or right.
  Create algorithm to calculate how many routes you can travel to the goal on a grid with dimensions m*n.
'''
def solution1(m, n):
  if m == 1 and n == 1: return 1
  if m == 0 or n == 0: return 0
  return solution1(m - 1, n) + solution1(m, n-1)

def solution2(m, n, memo={}):
  key = str(m) + "," + str(n)
  if key in memo: return memo[key]
  
  if m == 1 and n == 1: return 1
  if m == 0 or n == 0: return 0
  memo[key] = solution2(m - 1, n, memo) + solution2(m, n - 1, memo)
  return memo[key]

def solution3(m, n):
  # Create and initialize a travel grid.
  travel_grid = []
  for i in range(m+1):
    travel_grid.append([0] * (n+1)) # Set up a starting value
  travel_grid[1][1] = 1
  for i in range(m+1):
    for j in range(n+1):
      if i <= 1 and j <= 1:
        continue
      prev_row = travel_grid[i-1][j] if i >= 1 else 0
      prev_col = travel_grid[i][j-1] if j >= 1 else 0
      travel_grid[i][j] = prev_row + prev_col
  return travel_grid[m][n] 
      
