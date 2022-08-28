#%%
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

n = 4
Solution().fib(n)
# %%
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
n = 25
Solution().tribonacci(n)
# %%
