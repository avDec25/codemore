from typing import List
import functools

class Solution:
    def removeBoxes(self, a: List[int]) -> int:
        @functools.lru_cache(None)
        def remb(i, j, k):
            if i > j: return 0
            s = 0
            while (i+s) <= j and a[i] == a[s+i]:
                s += 1
            i2 = s+i                            # s already has +1, because of being loop counter
            res = remb(i2, j, 0) + (k+s)**2     # s already has +1, because of being loop counter
            for m in range(i2, j+1):
                if a[i] == a[m]:
                    res = max(res, remb(i2, m-1, 0) + remb(m, j, k+s))
            return res

        return remb(0, len(a)-1, 0)

        
boxes = [3, 3, 1, 3, 3]
Solution().removeBoxes(boxes)