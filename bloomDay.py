from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days):
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k            
            return bonquets >= m


        if m*k > len(bloomDay):
            return -1
            
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        
        return left


bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
Solution().minDays(bloomDay, m, k)
