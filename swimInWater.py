from typing import List
import heapq

class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    ans = 0
    N = len(grid)
    pq = [(grid[0][0], 0, 0)]
    visited = {(0, 0)}

    while pq:
      data = list(pq)
      print(data[0])
      d, r, c = heapq.heappop(pq)
      ans = max(d, ans)
      if r == N-1 and c == N-1:
        return ans
      else:
        for x, y in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
          if 0 <= x < N and 0 <= y < N and (x,y) not in visited:
            visited.add((x,y))
            heapq.heappush(pq, (grid[x][y], x, y))



grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Solution().swimInWater(grid)