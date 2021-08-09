from typing import List
import math
import bisect

class Solution:
    def maxSumSubmatrix(self, a: List[List[int]], k: int) -> int:
        ans = - math.inf
        H = len(a)
        W = len(a[0])

        def subArrSumAtMaxK(arr):
            res = - math.inf
            cumm_sum = 0
            prefix_sum = [math.inf]

            for x in arr:
                bisect.insort(prefix_sum, cumm_sum)
                cumm_sum += x
                i = bisect.bisect_left(prefix_sum, cumm_sum-k)
                res = max(res, cumm_sum - prefix_sum[i])
            return res

        for r in range(H):
            for c in range(W - 1):
                a[r][c + 1] += a[r][c]

        for L in range(W):
            for R in range(L, W):
                arr = [
                    a[x][R] - (a[x][L - 1] if L > 0 else 0) for x in range(H)
                ]
                ans = max(ans, subArrSumAtMaxK(arr))
        return ans


matrix = [[1, 0, 1], [0, -2, 3]]
k = 2
Solution().maxSumSubmatrix(matrix, k)
