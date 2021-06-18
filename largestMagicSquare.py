from typing import List

class Solution:
  def largestMagicSquare(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    rows = [[0]*(C+1) for _ in range(R)]
    cols = [[0]*(C)   for _ in range(R+1)]

    for r in range(R):
      for c in range(C):
        rows[r][c+1] = grid[r][c] + rows[r][c]
        cols[r+1][c] = grid[r][c] + rows[r][c]
    
    ans = 1
    for i in range(R):
      for j in range(C):
        diag = grid[i][j]
        for k in range(min(i, j)):
          ii, jj = i-k-1, j-k-1
          diag += grid[ii][jj]
          ss = {diag}
          for r in range(ii, i+1): ss.add(rows[r][j+1] - rows[r][jj])
          for c in range(jj, j+1): ss.add(rows[i+1][C] - rows[ii][c])
          ss.add(sum(grid[ii+kk][j-kk] for kk in range(k+2)))
          if len(ss) == 1: ans = max(ans, k+2)
    return ans


grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Solution().largestMagicSquare(grid)