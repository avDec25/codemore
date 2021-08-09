from typing import List
from functools import lru_cache

# class Solution:
#   def minCostClimbingStairs(self, cost: List[int]) -> int:
#     n = len(cost)
#     ans = 0

#     dp = {}
#     def reachTop(i):
#       if i in dp:
#         return dp[i]
#       if n <= i:
#         return 0
      
#       dp[i] = cost[i] + min(reachTop(i+1), reachTop(i+2))
#       return dp[i]

#     ans = min(reachTop(0), reachTop(1))
#     return ans

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    ans = 0

    def reachTop(i):
      if n <= i:
        return 0
      
      return cost[i] + min(reachTop(i+1), reachTop(i+2))

    ans = min(reachTop(0), reachTop(1))
    return ans


cost = [1,100,1,1,1,100,1,1,100,1]
Solution().minCostClimbingStairs(cost)