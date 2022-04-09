from typing import List


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:      
    self.n = n
    # r = 0
    # c = 0
    def isSafe(r, c):
      for ic in range(c):
        if self.board[r][ic] == 'Q':
          return False

      for ir, ic in zip(range(r, -1, -1), range(c, -1, -1)):
        if self.board[ir][ic] == 'Q':
          return False

      for ir, ic in zip(range(r, self.n, 1), range(c, -1, -1)):
        if self.board[ir][ic] == 'Q':
          return False

      return True

    def solveBoard(c):
      if c >= self.n: return True
      for ir in range(self.n):
        if isSafe(ir, c):
          self.board[ir][c] = 'Q'
          if solveBoard(c+1):
            return True
          self.board[ir][c] = '.'
      return False

    
    self.board = [['.' for _ in range(self.n)] for _ in range(self.n)]      
    if solveBoard(0) == False:
      return False
    else:
      result = []
      for i in range(self.n):
        result.append(''.join(self.board[i]))
      print(result)
      return True

n = 4
Solution().solveNQueens(n)
