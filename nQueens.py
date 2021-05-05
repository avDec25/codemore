from typing import List


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    board = []
    for _ in range(n): board.append([0] * n)
    
    
    return board
      

n = 4
Solution().solveNQueens(n)
