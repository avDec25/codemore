from typing import List
import math

class Solution:
    def minimumTotal(self, a: List[List[int]]) -> int:
        H = len(a)
        for i in range(H):
            for j in range(i+1):
            #     print((i, j), end="")
            #     print(f"min(a[{i-1}][{j-1}], a[{i-1}][{j}])")
            # print("")
                if i-1 < 0:
                    pass
                elif j-1 < 0:
                    a[i][j] += a[i-1][j]
                else:
                    a[i][j] += min(a[i-1][j-1], a[i-1][j] if j != len(a[i-1]) else math.inf)
        
        # print(a)
        return min(a[H-1][j] for j in range(len(a[H-1])))

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
Solution().minimumTotal(triangle)