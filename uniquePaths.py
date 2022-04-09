from functools import lru_cache
from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
    # @lru_cache(None)
    # def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
    #     if i >=m or j >= n: return 0
    #     if i==m-1 and j==n-1: return 1
    #     return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)

m = 3
n = 7
Solution().uniquePaths(m, n)