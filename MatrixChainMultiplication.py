#%%
# Matrix Chain Multiplication
import functools
class Solution:
    @functools.lru_cache(None)
    def solve(self, i, j):
        if i >= j: return 0
        ans = float("inf")
        for k in range(i, j):
            left_solved = self.solve(i, k)
            right_solved = self.solve(k+1, j)
            combine = self.a[i-1] * self.a[k] * self.a[j]
            ans = min(ans, left_solved + right_solved + combine)
        return ans
    
    def mcm(self, a):
        i = 1
        j = len(a)-1
        self.a = a
        return self.solve(i, j)
        
a = [40, 20, 30, 10, 30]
Solution().mcm(a)

# %%
# Palindrome Partitioning
import timeit
import functools
class Solution:
    def isPalindrome(self, i, j):
        for x in range(0, (j-i+1)//2+1):
            if self.s[i+x] != self.s[j-x]: return False
        return True
    
    @functools.lru_cache(None)
    def mcm(self, i, j):
        if i >= j or self.isPalindrome(i, j):
            return 0
        ans = float("inf")
        for k in range(i, j):
            left_solved = self.mcm(i, k)
            right_solved = self.mcm(k+1, j)
            ans = min(ans, 1 + left_solved + right_solved)
        return ans
    
    def minCut(self, s: str) -> int:
        self.s = s
        return self.mcm(0, len(s)-1)
        
S = "sdajfkdjsflkj"
start = timeit.default_timer()
print(Solution().minCut(S))
print(f"Time taken = { timeit.default_timer() - start}")


# %%
# Evaluate Expression to True
class Solution:
    def countWays(self, N, S):
        

S = "T|T&F^T"
Solution().countWays(len(S), S)
# %%
# Egg Dropping problem
# minimize the number of times you have to drop the eggs 
# to find the critical floor where critical floor means 
# the floor beyond which eggs start to break
import functools
class Solution:
    @functools.lru_cache(None)
    def superEggDrop(self, e: int, f: int) -> int:
        if f == 0 or f == 1 or e == 1:
            return f
        ans = float("inf")
        for k in range(1, f+1):
            t = 1 + max( self.superEggDrop(e-1, k-1), self.superEggDrop(e, f-k) )
            ans = min(t, ans)
        return ans
k = 3
n = 14
Solution().superEggDrop(k, n)
# %%
