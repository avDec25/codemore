#%%
# Climbing Stairs
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0: return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)

n = 6
Solution().climbStairs(n)
# %%
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.n = len(self.cost)
        def f(i):
            if i == n-1: return self.cost[i]
            if i >= n: return float('inf')
            return self.cost[i] + min(f(i+1), f(i+2))
        return min(f(0), f(1))

cost = [1,100,1,1,1,100,1,1,100,1]
Solution().minCostClimbingStairs(cost)
# %%
