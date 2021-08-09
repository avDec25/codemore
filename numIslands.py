from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    ans = 0

    H = len(grid)
    W = len(grid[0])

    visited = [[False for _ in range(W)] for _ in range(H)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def isSafe(x, y) -> bool:
      return 0 <= x < H and 0 <= y < W

    def bfs(i, j):
      visited[i][j] = True
      q = list()
      q.append((i,j))

      while len(q) > 0:
        x, y = q.pop(0)
        for dx, dy in moves:
          nx, ny = x+dx, y+dy
          if isSafe(nx, ny) and visited[nx][ny] == False and grid[nx][ny] == "1":
            visited[nx][ny] = True
            q.append((nx, ny))


    for i in range(H):
      for j in range(W):
        if grid[i][j] == "1" and not visited[i][j]:
          ans += 1
          bfs(i, j)

    return ans

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Solution().numIslands(grid)