from typing import List
import heapq  # brings minHeap


class Solution:
  def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    ans = 0
    sSum = 0
    h = []
    for e, s in sorted(zip(efficiency, speed), reverse=True):
      heapq.heappush(h, s)
      sSum += s
      if len(h) > k:
        sSum -= heapq.heappop(h)
      ans = max(ans, sSum * e)

    return ans


n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
Solution().maxPerformance(n, speed, efficiency, k)