# Reduce Array Size to The Half
from typing import Counter, List

class Solution:
    def minSetSize(self, a: List[int]) -> int:
        total = 0
        for i, freq in enumerate(sorted(Counter(a).values(), reverse=True)):
            print(i, freq)
            total += freq
            if total >= len(a)//2:
                return i + 1
        return 0

a = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
Solution().minSetSize(a)
