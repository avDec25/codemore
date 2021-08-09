from typing import List

class Solution:
    def numSubmatrixSumTarget(self, a: List[List[int]], target: int) -> int:
        ans = 0
        H = len(a)
        W = len(a[0])

        def subArrSumToK(arr):
            res = 0
            cumm_sum = 0
            prefix_sum = {0: 1}
            for x in arr:
                cumm_sum += x
                res += prefix_sum.get(cumm_sum-target, 0)
                prefix_sum[cumm_sum] = prefix_sum.get(cumm_sum, 0) + 1
            return res

        for r in range(H):
            for c in range(W-1):
                a[r][c+1] += a[r][c]

        for L in range(W):
            for R in range(L, W):
                arr = [
                    a[x][R] - (a[x][L-1] if L > 0 else 0)
                    for x in range(H)
                ]
                ans += subArrSumToK(arr)

        return ans

matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
Solution().numSubmatrixSumTarget(matrix, target)
