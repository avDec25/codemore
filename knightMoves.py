class Solution:
  def knightProbability(self, n: int, K: int, row: int, column: int) -> float:
    moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    mem = {}
    
    def dfs(k, x, y, P):
      p = 0
      if 0 <= x < n and 0 <= y < n:
        if k < K:
          for dx, dy in moves:
            _x = x + dx
            _y = y + dy
            if (_x, _y, k+1) not in mem:
              mem[(_x, _y, k+1)] = dfs(k+1, _x, _y, P/len(moves))
            p += mem[(_x, _y, k+1)]
        else:
          p = P
      return p

    return dfs(0, row, column, 1.0)
    

n, k, row, column = 8, 30, 6, 4
Solution().knightProbability(n, k, row, column)
