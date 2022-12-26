# %%
# 509. Fibonacci Number
from typing import List
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


n = 4
Solution().fib(n)
# %%


class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        dp = [0 for _ in range(n+1)]
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
# 0/1 KnapSack


class Solution:
    def knapSack(self, n, W, wt, val):
        t = [[0 for _ in range(W+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    t[i][j] = max(val[i-1] + t[i-1][j - wt[i-1]], t[i-1][j])
                elif wt[i-1] > j:
                    t[i][j] = t[i-1][j]
        return t[n][W]


N = 3
W = 4
values = [1, 2, 3]
weight = [4, 5, 1]
Solution().knapSack(N, W, weight, values)
# %%
# Subset sum


class Solution:
    def subsetsum(self, a, S) -> bool:
        n = len(a)
        t = [[False for _ in range(S+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(S+1):
                if i == 0:
                    t[i][j] = False
                if j == 0:
                    t[i][j] = True

        for i in range(1, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    t[i][j] = t[i-1][j] or t[i-1][j-a[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][S]


A = [3, 34, 4, 12, 5, 2]
B = 30
A = [3, 34, 4, 12, 5, 2]
B = 9
Solution().subsetsum(A, B)
# %%
# Equal Sum Partition


class Solution:
    def subsetSum(self, a, S) -> bool:
        n = len(a)
        t = [[False for _ in range(S+1)] for _ in range(n+1)]
        for j in range(S+1):
            t[0][j] = False
        for i in range(n+1):
            t[i][0] = True

        for i in range(1, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    t[i][j] = t[i-1][j] or t[i-1][j - a[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][S]

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        return self.subsetSum(nums, total_sum // 2)


nums = [1, 5, 11, 5]
Solution().canPartition(nums)

# %%
# Count of Subset


class Solution:
    def subsetSumToTarget(self, a: List[int], target: int) -> int:
        n = len(a)
        W = target
        T = [[0 for _ in range(W+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i == 0:
                    T[i][j] = 0
                if j == 0:
                    T[i][j] = 1

        for i in range(1, n+1):
            for j in range(1, W+1):
                if a[i-1] <= j:
                    T[i][j] = T[i-1][j] + T[i-1][j-a[i-1]]
                else:
                    T[i][j] = T[i-1][j]

        return T[n][W]


nums = [2, 3]
target = 3
Solution().subsetSumToTarget(nums, target)

# %%
# Minimum Subset Sum Difference
import math
class Solution:
    def minimumDifference(self, a: List[int]) -> int:
        n = len(a)
        W = sum(a)
        T = [[False for _ in range(W+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(W+1):
                if i == 0:
                    T[i][j] = False
                if j == 0:
                    T[i][j] = True

        for i in range(1, n+1):
            for j in range(1, W+1):
                if a[i-1] <= j:
                    T[i][j] = T[i-1][j] or T[i-1][j-a[i-1]]
                else:
                    T[i][j] = T[i-1][j]
        
        SS = [j for j in range(W+1) if T[n][j]]
        ans = math.inf
        for s1 in SS:
            if s1 > W//2: break
            ans = min(ans, W-2*s1)
        return ans

nums = [3, 9, 7, 3]
Solution().minimumDifference(nums)
# %%
# Count pairs of subsets with a given difference
class Solution:
    def countSubsetSum(self, a: List[int], S: int) -> int:
        n = len(a)
        T = [[0 for _ in range(S+1)] for _ in range(n+1)]
        
        # this is a fix for presence of zero elements in the array
        # with which subsets of different lengths can also be formed
        zc = [0]
        for i in range(1, len(a)+1):
            if a[i-1] == 0: zc.append(zc[i-1]+1)
            else: zc.append(zc[i-1])
        
        for i in range(n+1):
            for j in range(S+1):
                if i == 0: T[i][j] = 0
                if j == 0: T[i][j] = pow(2, zc[i])
        
        for i in range(1, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    T[i][j] = T[i-1][j] + T[i-1][j-a[i-1]]
                else:
                    T[i][j] = T[i-1][j]
        
        return T[n][S]
    
    def givenDifference(self, a: List[int], diff: int) -> int:
        S = (diff + sum(a)) // 2
        return self.countSubsetSum(a, S)

a = [1, 1, 2, 3]
diff = 1
Solution().givenDifference(a, diff)
# %%
# Target Sum
class Solution:
    def countSubsetSum(self, a: List[int], S: int) -> int:
        n = len(a)
        T = [[0 for _ in range(S+1)] for _ in range(n+1)]
        
        zc = [0]
        for i in range(1, len(a)+1):
            if a[i-1] == 0: zc.append(zc[i-1]+1)
            else: zc.append(zc[i-1])
        
        for i in range(n+1):
            for j in range(S+1):
                if i == 0: T[i][j] = 0
                if j == 0: T[i][j] = pow(2, zc[i])
        
        for i in range(1, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    T[i][j] = T[i-1][j] + T[i-1][j-a[i-1]]
                else:
                    T[i][j] = T[i-1][j]
        
        return T[n][S]
    
    def givenDifference(self, a: List[int], diff: int) -> int:
        total_sum = sum(a)
        if (diff > total_sum) or ((total_sum + diff) % 2 != 0) : return 0
        S = (total_sum + diff) // 2
        return self.countSubsetSum(a, S)
    
    def findTargetSumWays(self, a: List[int], target: int) -> int:
        return self.givenDifference(a, abs(target))
        
nums = [1000]
target = -1000
Solution().findTargetSumWays(nums, target)

# %%
# Unbounded Knapsack: Rod Cutting Problem
class Solution:
    def cutRod(self, price, n):
        T = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i <= j:
                    T[i][j] = max(T[i-1][j], price[i-1] + T[i][j-i])
                else:
                    T[i][j] = T[i-1][j]
        return T[n][n]
  
# length of rod
N = 8
# for piece of length i; it's price is given as price[i]
price = [1, 5, 8, 9, 10, 17, 17, 20]
Solution().cutRod(price, N)

# %%
# Coin Change I
# https://practice.geeksforgeeks.org/problems/coin-change2448
class Solution:
    def coinChangeI(self, coins: List[int], S: int) -> int:
        n = len(coins)
        T = [[0 for _ in range(S+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(S+1):
                if i == 0: T[i][j] = 0
                if j == 0: T[i][j] = 1
        
        for i in range(1, n+1):
            for j in range(1, S+1):
                if coins[i-1] <= j:
                    T[i][j] = T[i-1][j] + T[i][j - coins[i-1]]
                else:
                    T[i][j] = T[i-1][j]
        return T[n][S]
    
# unlimited supply of coins, find number of ways to get amount
coins = [2, 5, 3, 6]
amount = 10
Solution().coinChangeI(coins, amount)

# %%
# Coin Change II: minimum number of coins to be chosen such the sum is obtained
# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, a: List[int], S: int) -> int:
        n = len(a)
        INF = 2**32-1
        T = [[INF for _ in range(S+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(S+1):
                if i == 0: T[i][j] = INF
                if j == 0: T[i][j] = 0
        
        for j in range(1, S+1):
            if j % a[0] == 0:
                T[1][j] = j // a[0]
            else:
                T[1][j] = INF
        
        for i in range(2, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    T[i][j] = min(T[i-1][j], 1 + T[i][j - a[i-1]])
                else:
                    T[i][j] = T[i-1][j]
        
        return T[n][S] if T[n][S] < INF else -1
    
coins = [2]
amount = 3
Solution().coinChange(coins, amount)
