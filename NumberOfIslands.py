from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H = len(grid)
        W = len(grid[0])

        visited = set()
        def mark_connected_as_visited(i, j):
            visited.add((i,j))
            q = deque([(i,j)])
            while q:
                r, c = q.popleft()
                for x, y in [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]:
                    if 0 <= x < H and 0 <= y < W and (x,y) not in visited and grid[x][y] == "1":
                        visited.add((x,y))
                        q.append((x,y))
        
        ans = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    mark_connected_as_visited(i, j)
        return ans


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
Solution().numIslands(grid) 
