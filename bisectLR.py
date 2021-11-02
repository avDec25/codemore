from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
# from bisect import bisect, bisect_left, bisect_right

# a = [0, 1, 3, 3, 4]
# x = 3
# res_bisect = bisect(a, x)
# res_bisect_left = bisect_left(a, x)
# res_bisect_right = bisect_right(a, x)
# console.log(log_locals=True)

# import re
# expression = "-1/2+3-6/7*10-5"
# re.findall('[+-]?\d+', expression)

# ans = []
# def allSubsequence(i, o):
#     if len(i) == 0:
#         ans.append(o)
#         return
#     allSubsequence(i[1:], o+i[0])
#     allSubsequence(i[1:], o)

# w = "abcdefgh"
# allSubsequence(w, "")
# print(ans)

w = "abcdefghijkhmnopqustuvwxyz"
for i in range(len(w)+1)[:0:-1]:
    print(i, end=' ')
from typing import List
from collections import defaultdict

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