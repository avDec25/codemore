import functools

class Solution:
    def climbStairs(self, n: int) -> int:
        @functools.lru_cache(None)
        def ways(i):
            if i < 0: return 0
            if i < 2: return 1
            return ways(i-1) + ways(i-2)
        return ways(n-1) + ways(n-2)

n = 2
Solution().climbStairs(n)
