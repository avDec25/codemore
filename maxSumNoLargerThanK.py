# Max Sum of Rectangle No Larger Than K
from typing import List
import math
import bisect

class Solution:
    def maxSumSubmatrix(self, a: List[List[int]], k: int) -> int:
        H = len(a)
        W = len(a[0])

        def maxSubArrMaxK(arr, k):
            max_so_far = -math.inf
            cumm_sum = 0
            prefix_sum = [math.inf]

            for x in arr:
                bisect.insort(prefix_sum, cumm_sum)
                cumm_sum += x
                i = bisect.bisect_left(prefix_sum, cumm_sum - k)
                max_so_far = max(max_so_far, cumm_sum - prefix_sum[i])
            return max_so_far


        res = -math.inf
        for r in range(H):
            for c in range(W-1):
                a[r][c+1] += a[r][c]

        for y1 in range(W):
            for y2 in range(y1, W):
                arr = [
                    a[x][y2] - (a[x][y1-1] if y1 > 0 else 0)
                    for x in range(H)
                ]
                res = max(res, maxSubArrMaxK(arr, k))

        return res


matrix = [[1, 0, 1], [0, -2, 3]]
k = 2
Solution().maxSumSubmatrix(matrix, k)
