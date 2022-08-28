#%%
# 509. Fibonacci Number
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n <= 1: return n
        return self.fib(n-1) + self.fib(n-2)

n = 4
Solution().fib(n)
# %%
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2: return 1
        dp = [ 0 for _ in range(n+1) ]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        i = 3
        while i <= n:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            i += 1
        return dp[n]

n = 25
Solution().tribonacci(n)
# %%
