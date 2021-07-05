from typing import List

class Solution:
    def gray_code_generator(self, n: int) -> List[List[int]]:
        res = [0]
        for i in range(n):
            for x in reversed(res):
                res += [ x | (1<<i) ]
        return res

n = 2
Solution().gray(n)
res = [1, 2, 3, 4, 5]
print([x for x in reversed(res)])