from typing import List


class UF:
  def __init__(self, n) -> None:
    self.n = n
    self.id = list(range(n))
    self.size = [1] * n
    self.cc = n             # connected components
  
  def connectedComponents(self):
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

uf = UF(10)
uf.union(5, 3)
print(uf)
