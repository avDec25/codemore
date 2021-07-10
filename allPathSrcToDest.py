from typing import List
from collections import defaultdict

class Solution:
  def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adjList = defaultdict(set)
    visited = defaultdict(int)
    for u,v in edges:
      adjList[u].add(v)
    
    def dfs(node):
      if visited[node] == -1:
        return False
      elif visited[node] == 1:
        return True
      elif len(adjList[node]) == 0:
        return node == destination
      else:
        visited[node] = -1
        for child in adjList[node]:
          if not dfs(child):
            return False
        visited[node] = 1
        return True
    
    return dfs(source)


n = 4
edges = [[0,1],[0,2],[1,3],[2,3]]
source = 0
destination = 3
Solution().leadsToDestination(n, edges, source, destination)