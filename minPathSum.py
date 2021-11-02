from typing import List
import math

class Solution:
    def minPathSum(self, a: List[List[int]]) -> int:
        H = len(a)
        W = len(a[0])
        # dp = [[0 for _ in range(W)] for _ in range(H)]
        
        # dp[0][0] = a[0][0]
        for i in range(0, H):
            for j in range(0, W):
                if i-1 == -1 and j-1 == -1:
                    a[i][j] = a[i][j]
                elif i-1 == -1:
                    a[i][j] = a[i][j] + a[i][j-1]
                elif j-1 == -1:
                    a[i][j] = a[i][j] + a[i-1][j]
                else:
                    a[i][j] = a[i][j] + min(a[i-1][j] if i-1>=0 else math.inf, a[i][j-1] if j-1>=0 else math.inf)
        return a[H-1][W-1]

    # def mps(self, a: List[List[int]]) -> int:



grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1]]
Solution().minPathSum(grid)
# Solution().mps(grid)