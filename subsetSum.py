#%% 
# Subset Sum
# Check if a subset with the target sum exists?

class Solution:
    def isSubsetSum(self, n, a, S):
        t = [[False for _ in range(S+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(S+1):
                if i == 0: t[i][j] = False
                if j == 0: t[i][j] = True
        
        for i in range(1, n+1):
            for j in range(1, S+1):
                if a[i-1] <= j:
                    t[i][j] = t[i-1][j] or t[i-1][j-a[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        return t[n][S]

arr = [3, 34, 4, 12, 5, 2]
s = 9
Solution().isSubsetSum(len(arr), arr, s)
# %%
 