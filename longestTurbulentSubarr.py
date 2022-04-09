from typing import List

class Solution:
    def maxTurbulenceSize(self, a: List[int]) -> int:
        best = streak = 0
        for i in range(len(a)):
            if i >= 2 and (a[i-2] > a[i-1] < a[i] or a[i-2] < a[i-1] > a[i]):
                streak += 1
            elif i >= 1 and a[i-1] != a[i]:
                streak = 2
            else:
                streak = 1
            best = max(best,  streak)
        return best


a = [4, 8, 12, 16]
Solution().maxTurbulenceSize(a)
