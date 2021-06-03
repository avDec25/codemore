from typing import List
import sys

class Solution:
  def minCost(self, costs: List[List[int]]) -> int:
    ans = sys.maxsize
    H = len(costs)
    W = len(costs[0])

    def excluding(x, y):
      if x >= H:
        return 0
      sol = sys.maxsize
      for j in range(W):
        if j != y:
          sol = min(sol, costs[x][j] + excluding(x+1, j))
      return sol
    

    for j in range(W):
      ans = min(ans, costs[0][j] + excluding(1, j))

    return ans

costs = [[2,11,9],[10,18,19],[6,2,15],[4,13,14],[12,14,14],[12,2,8],[20,13,4],[14,2,13],[4,4,18],[20,19,3],[20,2,8],[2,5,6],[16,1,1],[10,12,12],[9,6,20],[14,9,19],[7,8,13],[6,19,15],[18,14,14],[7,4,17],[20,16,10],[10,15,2]]
Solution().minCost(costs)