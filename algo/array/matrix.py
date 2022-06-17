'''
  Write a function that accepts an integer n and returns a N x N spiral matrix.
  Example: 
  matrix(2)
    [[1, 2],
    [4, 3]]
  matrix(3)
    [[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]
  matrix(4)
    [[1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]]
'''

def solution(n):
  matrix = [[0]*n for _ in range(n)] 
  startRow = 0
  startCol = 0
  endRow = n-1
  endCol = n-1
  counter = 1
  while startCol <= endCol and startRow <= endRow:
    for i in range(startCol, endCol+1):
      # from-left-to-right row
      matrix[startRow][i] = counter
      counter += 1
    startRow += 1
    
    for i in range(startRow, endRow+1):
      # from-top-to-bottom column
      matrix[i][endCol] = counter
      counter += 1
    endCol -= 1

    for i in range(endCol, startCol-1, -1):
      matrix[endRow][i] = counter
      counter += 1
    endRow -= 1

    for i in range(endRow, startRow-1, -1):
      matrix[i][startCol] = counter
      counter += 1
    startCol +=1

  return matrix
