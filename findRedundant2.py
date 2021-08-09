from collections import defaultdict, deque
from typing import List

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    adjList = defaultdict(list)
    for edge in edges:
      adjList[edge[0]].append(edge[1])

    for edge in edges:
      u = edge[0]
      v = edge[1]
      adjList[u].remove(v)

      isPartOfCycle = False
      q = deque()
      visited = set()
      q.append(u)
      visited.add(u)
      while q:
        f = q.popleft()
        if f == v:
          isPartOfCycle = True
          break
        for neighbour in adjList[f]:
          if neighbour not in visited:
            q.append(neighbour)
            visited.add(neighbour)

      if isPartOfCycle:
        return edge

      adjList[u].append(v)
    return []

edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Solution().findRedundantConnection(edges)