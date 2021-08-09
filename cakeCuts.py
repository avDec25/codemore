from typing import List
import math

class Solution:
  def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    if 0 not in horizontalCuts:
      horizontalCuts.append(0)
    if h not in horizontalCuts:
      horizontalCuts.append(h)
    horizontalCuts.sort()

    if 0 not in verticalCuts:
      verticalCuts.append(0)
    if w not in verticalCuts:
      verticalCuts.append(w)
    verticalCuts.sort()

    hMxDiff = 0
    vMxDiff = 0

    for i in range(1, len(horizontalCuts)):
      hMxDiff = max(horizontalCuts[i] - horizontalCuts[i-1], hMxDiff)

    for j in range(1, len(verticalCuts)):
      vMxDiff = max(verticalCuts[j] - verticalCuts[j-1], vMxDiff)

    return (vMxDiff * hMxDiff) % (10**9 + 7)

h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]
Solution().maxArea(h, w, horizontalCuts, verticalCuts)

