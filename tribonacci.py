from functools import lru_cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def t(i):
            if i <= 0: return 0
            if i < 3: return 1
            return t(i-1) + t(i-2) + t(i-3)
        return t(n)

n = 25
Solution().tribonacci(n)