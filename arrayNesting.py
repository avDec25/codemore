from typing import List

class Solution:
    def arrayNesting(self, a: List[int]) -> int:
        seen, res = [False] * len(a), 0
        for i in a:
            cnt = 0
            while not seen[i]:
                seen[i] = True
                cnt += 1
                i = a[i]
            res = max(res, cnt)
        return res


nums = [5, 4, 0, 3, 1, 6, 2]
Solution().arrayNesting(nums)