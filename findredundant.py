from typing import List


class UF:
  def __init__(self, n) -> None:
    self.n = n
    self.id = list(range(n))
    self.size = [1] * n
    self.cc = n             # connected components
  
  def connected_components(self):
    return self.cc

  def find(self, p):
    if self.id[p] == p:
      return p

    self.id[p] = self.find(self.id[p])
    return self.id[p]
  
  def union(self, p, q):
    rp = self.find(p)
    rq = self.find(q)

    if rp == rq:
      return False    

    if self.size[rp] < self.size[rq]:
      self.id[rp] = rq
      self.size[rq] += self.size[rp]
    else:
      self.id[rq] = rp
      self.size[rp] += self.size[rq]
    
    self.cc -= 1
    return True

  def isConnected(self, p, q):
    return self.find(p) == self.find(q)
  
  def componentSize(self, p):
    rp = self.find(p)
    return self.size[rp]

  def __str__(self) -> str:
    ans = "UnionFind DS:\n"
    for i in range(self.n):
      ans += f'item: {i}, root: {self.id[i]}, size: {self.size[self.find(i)]}\n'
    return ans
  
  def __repr__(self) -> str:
    return f'UF({str(self)})'


class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    ans = []

    # this works because in a graph containing atleast 1 cycle, the total edges will be atleast v
    uf = UF(len(edges))

    for x, y in edges:
      if not uf.union(x - 1, y - 1): 
        ans = [x, y]

    return ans


edges = [[6,13],[15,22],[10,13],[12,24],[3,23],[19,20],[3,12],[2,16],[19,23],[2,11],[18,23],[1,25],[2,17],[4,5],[14,19],[2,3],[1,7],[4,6],[9,10],[8,22],[7,22],[13,18],[13,21],[15,23],[5,25]]
Solution().findRedundantConnection(edges)
