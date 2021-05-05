from typing import List
import collections

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:    
    adjList = collections.defaultdict(set)
    for edge in edges:
      u = edge[0]
      v = edge[1]
      adjList[u].add(v)
      adjList[v].add(u)
    
    visited = [False] * n    
    ans = 0
    
    for v in range(n):
      queue = []
      if not visited[v]:
        ans += 1
        queue.append(v)
        visited[v] = True
      
      while len(queue) > 0:
        popped = queue.pop(0)
        for neighbour in adjList[popped]:
          if not visited[neighbour]:
            queue.append(neighbour)
            visited[neighbour] = True
    
    return ans



n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

sol = Solution()
ans = sol.countComponents(n, edges)
print(ans)
