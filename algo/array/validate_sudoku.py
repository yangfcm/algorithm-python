'''
   Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
   validated according to the following rules: 
   1 - Each row must contain the digits 1-9 without repetition. 
   2 - Each column must contain the digits 1-9 without repetition. 
   3 - Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition. 
  The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
  e.g. Input:
  [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
  ]
  Output: true
  Input:
  [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
  ]
  Output: false (There are two 8s in the first column)
'''
def solution(board):
  n = 9
  allowedNumbers = {'1','2','3','4','5','6','7','8','9'}
  for i in range(n):
    row = set()
    col = set()
    box = set()
    for j in range(n):  # Check rows
      if board[i][j] != '.':
        if not board[i][j] in allowedNumbers or board[i][j] in row:
          return False
        else:
          row.add(board[i][j])

      if board[j][i] != '.': # Check cols
        if not board[j][i] in allowedNumbers or board[j][i] in col:
          return False
        else:
          col.add(board[j][i])
      
      boxEl = board[3*(i//3) + j//3][3*(i%3) + (j%3)]
      if boxEl != '.':  # Check box
        if not boxEl in allowedNumbers or boxEl in box:
          return False
        else:
          box.add(boxEl)
  
  return True

          