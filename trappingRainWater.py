from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    ans = 0
    n = len(height)
    mxLeft = [0] * n
    mxRight = [0] * n
    
    mxL = 0
    for x in range(n):
      mxL = max(mxL, height[x])
      mxLeft[x] = max(mxL, height[x])
    
    mxR = 0
    for x in range(n-1, -1, -1):
      mxR = max(mxR, height[x])
      mxRight[x] = mxR
    
    for i in range(1, n-1):
      ans += abs(min(mxLeft[i], mxRight[i]) - height[i])
      
    return ans

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
