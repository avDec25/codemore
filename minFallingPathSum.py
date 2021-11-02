from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
from typing import List
import math

class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        H = len(a)
        W = len(a[0])

        for i in range(1, H):
            # print("============================================")
            for j in range(W):
                a[i][j] = a[i][j] + min(a[i-1][j+1] if (H > i-1 >= 0 and W > j+1 >= 0) else math.inf, 
                                        a[i-1][j] if (H > i-1 >= 0 and W > j >= 0) else math.inf, 
                                        a[i-1][j-1] if (H > i-1 >= 0 and W > j-1 >= 0) else math.inf)
                # console.log(log_locals=True)
        
        return min(a[-1])

# matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]
Solution().minFallingPathSum(matrix)