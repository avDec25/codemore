from collections import defaultdict, deque
from typing import List

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    ans = []
    adjList = defaultdict(list)
    for edge in edges:
      adjList[edge[0]].append(edge[1])
      adjList[edge[1]].append(edge[0])

    for edge in edges:
      u = edge[0]
      v = edge[1]
      adjList[u].remove(v)
      adjList[v].remove(u)

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
        ans = edge

      adjList[u].append(v)
      adjList[v].append(u)
    return ans


edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
Solution().findRedundantConnection(edges)
