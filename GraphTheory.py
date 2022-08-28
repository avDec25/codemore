#%%
# Flood Fill
from typing import List
from queue import Queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        q = Queue()
        q.put((sr, sc))
        while not q.empty():
            ex, ey = q.get()
            cc = image[ex][ey]
            image[ex][ey] = newColor
            for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = dx+ex, dy+ey
                if 0<=x<m and 0<=y<n and image[x][y]!=newColor and image[x][y]==cc:
                    q.put((x, y))
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
Solution().floodFill(image, sr, sc, newColor)
# %%
# Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        q = Queue()
        breakOut = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.put((i, j))
                    breakOut = True
                    break
            if breakOut:
                break
        while not q.empty():
            ex, ey = q.get()
            grid[ex][ey] = 2
            result += 1
            # mark all neighbours as visited
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = ex+dx, ey+dy
                if 0<=x<m and 0<=y<n and (grid[x][y]!=2 or grid[x][y]!=0):
                    q.put((x, y))
        return result

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Solution().numIslands(grid)
# %%
