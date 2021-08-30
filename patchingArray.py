from typing import List

class Solution:
    def minPatches(self, a: List[int], n: int) -> int:
        miss = 1
        added = 0
        i = 0
        while miss <= n:
            if i < len(a) and a[i] <= miss:
                miss += a[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added


nums = [1, 5, 10]
n = 20
Solution().minPatches(nums, n)