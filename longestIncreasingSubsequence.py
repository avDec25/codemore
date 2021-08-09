from typing import List
import math

class Solution:
  def lengthOfLIS(self, a: List[int]) -> int:
    piles = [[math.inf]]
    for x in a:
      inserted = False
      for pile in piles:
        if pile[-1] >= x:
          pile.append(x)
          inserted = True
          break
      if not inserted:
        piles.append([x])

    return len(piles)

nums = [10,9,2,5,3,7,101,18]
Solution().lengthOfLIS(nums)