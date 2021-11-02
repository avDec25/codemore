from typing import List
import functools

class Solution:
    def minCostClimbingStairs(self, a: List[int]) -> int:
        @functools.lru_cache(None)
        def f(i):
            if i < 2: return a[i]
            return a[i] + min(f(i-1), f(i-2))
        return min(f(len(a)-1), f(len(a)-2))

cost = [1,100,1,1,1,100,1,1,100,1]
Solution().minCostClimbingStairs(cost)
