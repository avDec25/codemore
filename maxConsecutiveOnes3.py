from typing import List

class Solution:
  def longestOnes(self, a: List[int], k: int) -> int:
    left = 0
    n = len(a)
    for right in range(n):      
      k -= 1 - a[right]   # k will decrement only if a[right] = 0
      if k < 0:
        k += 1 - a[left]  # k will be incremented only if a[left] = 0, 
                          # means we removed a 0 
                          # meaning we have removed a 0 from our window
        left += 1
    
    return right - left + 1

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
Solution().longestOnes(nums, k)