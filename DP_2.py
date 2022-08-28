#%%
# climbing stairs
from typing import List
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.cost = cost
        @lru_cache(None)
        def mcost(n):
            if n < 0: return 0
            if n <= 1: return self.cost[n]
            return self.cost[n] + min(mcost(n-1), mcost(n-2))
        return min(mcost(n-1), mcost(n-2))

cost = [1,100,1,1,1,100,1,1,100,1]
Solution().minCostClimbingStairs(cost)

# %%
# house rob
class Solution:
    def rob(self, a: List[int]) -> int:
        n = len(a)
        self.a = a
        @lru_cache(None)
        def njrob(n):
            if n < 0: return 0
            return max(a[n] + njrob(n-2), njrob(n-1))

        return max(njrob(n-2), njrob(n-1))

nums = [2,7,9,3,1]
Solution().rob(nums)

# %%
# house rob 2
class Solution:
    def rob(self, a: List[int]) -> int:
        def iRob(a):
            n = len(a)
            self.a = a
            @lru_cache(None)
            def njrob(n):
                if n < 0: return 0
                return max(a[n] + njrob(n-2), njrob(n-1))

            return max(njrob(n-2), njrob(n-1))
        return max(a[0] + iRob(a[2:-1]), iRob(a[1:]))

nums = [1, 2, 3, 1]
Solution().rob(nums)

# %%
# delete and earn
import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        a = [0] * 10001
        dp = [0] * 10001
        for k in c:
            a[k] = k*c[k]

        n = 10001
        dp[0] = a[0]
        dp[1] = a[1]
        for i in range(2, n):
            dp[i] = max(a[i] + dp[i-2], dp[i-1])

        return dp[n-1]

nums = [2,2,3,3,3,4]
Solution().deleteAndEarn(nums)
# %% 
# Jump Game
from typing import List
from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.n = len(nums)
        dp = dict()
        def jump(i):
            if i >= self.n-1: return True
            for x in range(1, nums[i]+1):
                if jump(i+x): return True
            return False
        return jump(0)

nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
Solution().canJump(nums)

# %%
# Jump Game
from typing import List
from functools import lru_cache
class Solution:
    def canJump(self, a: List[int]) -> bool:
        n = len(a)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            mxj = min(n-1, i+a[i])
            for j in range(i+1, mxj+1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0] 

nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
Solution().canJump(nums)

# %%
# Jump Game 2
from functools import lru_cache
class Solution:
    def jump(self, a: List[int]) -> int:
        n = len(a)

        @lru_cache(None)
        def jump2(i):
            val = float('inf')
            if i >= n-1: return 0
            for x in range(1, a[i]+1):
                val = min(1+jump2(i+x), val)
            return val

        return jump2(0)

nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
Solution().jump(nums)
# %%
class Solution:
    def jump(self, a: List[int]) -> int:
        n = len(a)
        dp = [n] * 10001
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(1, a[i]+1):
                dp[i] = min(dp[i], 1+ dp[min(i+j, n-1)])
        return dp[0]
nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
Solution().jump(nums)

# %%
# maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Solution().maxSubArray(nums)
# %%
