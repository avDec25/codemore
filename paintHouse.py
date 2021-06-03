from typing import List

class Solution:
  def minCost(self, costs: List[List[int]]) -> int:
    H = len(costs)
    for i in range(1, H):
      costs[i][0] += min(costs[i-1][1], costs[i-1][2])
      costs[i][1] += min(costs[i-1][0], costs[i-1][2])
      costs[i][2] += min(costs[i-1][0], costs[i-1][1])

    return min(costs[H-1][j] for j in range(3))


costs = [[2,11,9],[10,18,19],[6,2,15],[4,13,14],[12,14,14],[12,2,8],[20,13,4],[14,2,13],[4,4,18],[20,19,3],[20,2,8],[2,5,6],[16,1,1],[10,12,12],[9,6,20],[14,9,19],[7,8,13],[6,19,15],[18,14,14],[7,4,17],[20,16,10],[10,15,2]]
Solution().minCost(costs)