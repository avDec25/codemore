from typing import List
from itertools import accumulate
from functools import lru_cache

class Solution:
  def stoneGameVII(self, stones: List[int]) -> int:
    n = len(stones)
    memo = [[0]*n for _ in range(n)]
    sums = [0] + list(accumulate(stones))


    def dfs(l,r):
      if l == r:
        return 0
      
      if memo[l][r] == 0:
        rSum = sums[r+1] - sums[l]
        memo[l][r] = max(rSum - stones[l] - dfs(l+1, r), rSum - stones[r] - dfs(l, r-1))
      return memo[l][r]

    ans = dfs(0, n-1)
    print(memo)
    return ans

stones = [7,90,5,1,100,10,10,2]
Solution().stoneGameVII(stones)