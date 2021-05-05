from typing import List


class Solution:
  def trap(self, a: List[int]) -> int:
    ans = 0
    n = len(a)
    left, right, maxLeft, maxRight = 0, n-1, 0, 0
    while left <= right:
      if a[left] <= a[right]:
        maxLeft = max(maxLeft, a[left])
        ans += abs(maxLeft - a[left])
        left += 1
      else:
        maxRight = max(maxRight, a[right])
        ans += abs(maxRight - a[right])
        right -= 1
    return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
