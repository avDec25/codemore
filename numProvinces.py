from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    
    ######## union find functions ########
    parent = [i for i in range(n)]
    count = {}
    
    def uf_find(a):
      if a != parent[a]:
        parent[a] = uf_find(parent[a])
      return parent[a]
    
    def uf_union(a, b):
      ra = uf_find(a)
      rb = uf_find(b)
      if ra != rb:
        parent[ra] = rb
    
    def uf_connected(a, b):
      return uf_find(a) == uf_find(b)
    ######################################

    for i in range(n):
      for j in range(i+1, n):
        if isConnected[i][j] == 1:
          uf_union(i, j)

    for i in range(n):
      r = uf_find(i)
      count[r] = count.get(r, 0) + 1

    return len(count)



# adjacency matrix
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Solution().findCircleNum(isConnected)