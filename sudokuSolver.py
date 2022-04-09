from typing import List


class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:
    self.nr = len(board)
    self.nc = len(board[0])
    self.board = board
    
    def inRow(num, r, c):
      for ic in range(self.nc):
        if self.board[r][ic] == num:
          return True
      return False
    
    def inCol(num, r, c):
      for ir in range(self.nr):
        if self.board[ir][c] == num:
          return True
      return False
    
    def inSquare(num, r, c):
      for ir in range(r//3*3, r//3*3+3):
        for ic in range(c//3*3, c//3*3+3):
          if r != ir and ic != c and self.board[ir][ic] == num:
            return True
      return False
    
    def backtrack(r, c):
      if c == self.nc:
        r += 1
        c = 0

      if r == self.nr:
        return True

      if self.board[r][c] == '.':
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
          if not inRow(num, r, c) and not inCol(num, r, c) and not inSquare(num, r, c):
            self.board[r][c] = num
            if backtrack(r, c+1):
              return True
            self.board[r][c] = '.'
      else:
        return backtrack(r, c+1)

    backtrack(0, 0)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)