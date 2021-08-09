from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ksmallest = []
        H = len(matrix)
        W = len(matrix[0])
        for r in range(H):
            for c in range(W):
                heapq.heappush(ksmallest, matrix[r][c])                
        while k > 0:
            ans = heapq.heappop(ksmallest)
            k -= 1
        return ans


matrix = [[1, 2], [1, 3]]
k = 2
Solution().kthSmallest(matrix, k)
