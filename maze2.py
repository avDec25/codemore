from typing import List
import heapq

# Dijkstra Algorithm
class Solution:
  def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    H, W, q, stopped = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]): 0}
    while q:
      dist, x, y = heapq.heappop(q)
      if [x, y] == destination:
        return dist
      
      for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
        newX, newY, d = x, y, 0
        while 0 <= newX+dx < H and 0 <= newY+dy < W and maze[newX+dx][newY+dy] != 1:
          newX += dx
          newY += dy
          d += 1
        if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
          stopped[(newX, newY)] = dist + d
          heapq.heappush(q, (dist + d, newX, newY))

    return -1

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
Solution().shortestDistance(maze, start, destination)