from typing import List

class Solution:
  def maxSumRect(self, a: List[List[int]]) -> int:
    def kadane(runningRowSum):
      max_so_far = runningRowSum[0]
      current_max = runningRowSum[0]
      for i in range(1, H):
        current_max = max(current_max + runningRowSum[i], runningRowSum[i])
        max_so_far = max(max_so_far, current_max)
      return max_so_far

    H = len(a)
    W = len(a[0])
    ans = 0
    L = 0 
    R = 0
    for L in range(W):
      runningRowSum = [0] * H
      for R in range(L, W):
        for r in range(H):
          runningRowSum[r] += a[r][R]
        ans = max(ans, kadane(runningRowSum))
    return ans

matrix = [
  [6, -5, -7, 4, -4],
  [-9, 3, -6, 5, 2],
  [-10, 4, 7, -6, 3],
  [-8, 9, -3, 3, -7]
]
Solution().maxSumRect(matrix)
