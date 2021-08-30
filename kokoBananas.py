from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            return sum(math.ceil(pile / speed) for pile in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2
            if can_finish(mid):
                right = mid
            else:
                left = mid+1
        return left

piles = [30,11,23,4,20]
h = 6
Solution().minEatingSpeed(piles, h)
