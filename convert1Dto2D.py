from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        a2d = []
        k = 0
        for _ in range(m):
            a1d = []
            for _ in range(n):
                a1d.append(original[k])
                k += 1
            a2d.append(a1d)
        return a2d

original = [1,2]
m = 1
n = 1
Solution().construct2DArray(original, m, n)
