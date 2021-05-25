import collections


class Solution:
  def minKnightMoves(self, fx: int, fy: int) -> int:    
    moves = ((-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, 2), (2, 1), (1, -2), (2, -1))
    visited = dict()
    
    q = collections.deque()    
    q.append((0,0,0))
    visited[(0,0)] = True
    
    while q:
      x, y, d = q.popleft()
      if fx == x and fy == y:
          return d
      for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if not visited.get((nx,ny), False):
          visited[(nx, ny)] = True
          q.append((nx, ny, d+1))
    
x = 1
y = 1
Solution().minKnightMoves(x, y)
