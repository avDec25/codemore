from typing import List
import collections

class Solution:
  def shortestSubarray(self, a: List[int], k: int) -> int:
    d = collections.deque()  # stores possible values of the start pointer
    n = len(a)
    
    cs = [0] * (n+1)
    for i in range(n):
      cs[i+1] = cs[i] + a[i]
    
    ans = n+1
    for i in range(n+1):
      while d and cs[i] - cs[d[0]] >= k:
        ans = min(ans, i - d.popleft())
      
      # do no start subarray from an index which points to a negative integer in array, 
      # as K > 0 
      while d and cs[i] <= cs[d[-1]]:
        d.pop()
      
      d.append(i)
    
    return -1 if ans == n+1 else ans
    
    
     

A = [84, -37, 32, 40, 95]
K = 167
print(Solution().shortestSubarray(A, K))
