from typing import List
import collections


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ans = 0
    H = len(grid)
    W = len(grid[0])
    visited = [[False for _ in range(W)] for _ in range(H)]
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def isSafe(x, y) -> bool:
      return (0 <= x < H) and (0 <= y < W)

    def bfs(x, y):
      q = collections.deque()
      q.append((x, y))
      visited[x][y] = True
      sz = 1
      while len(q) > 0:
        fx, fy = q.popleft()
        for dx, dy in moves:
          nx = fx + dx
          ny = fy + dy
          if isSafe(nx, ny) and visited[nx][ny] == False and grid[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny))
            sz += 1
      return sz

    for i in range(H):
      for j in range(W):
        if not visited[i][j] and grid[i][j] == 1:
          ans = max(ans, bfs(i, j))

    return ans

grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Solution().maxAreaOfIsland(grid)