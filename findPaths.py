# Out of Boundary Paths
from collections import deque

class Solution:
  def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    MOD = 10**9 + 7
    ans = 0
    
    nxt = [[0] * n for _ in range(m)]
    nxt[startRow][startColumn] = 1

    for time in range(maxMove):
      cur = nxt
      nxt = nxt = [[0] * n for _ in range(m)]
      for r, row in enumerate(cur):
        for c, val in enumerate(row):
          for nr, nc in ((r,c+1), (r+1,c), (r-1,c), (r,c-1)):
            if 0 <= nr < m and 0 <= nc < n:
              nxt[nr][nc] += val
              nxt[nr][nc] %= MOD
            else:
              ans += val
              ans %= MOD

    return ans

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
Solution().findPaths(m, n, maxMove, startRow, startColumn)
