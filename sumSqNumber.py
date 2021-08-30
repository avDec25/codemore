import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = range(math.ceil(math.sqrt(c))+1)
        left = 0
        right = a[-1]
        while left <= right:
            sm = a[left]**2 + a[right]**2
            if sm == c:
                return True
            elif sm < c:
                left += 1
            else:
                right -= 1
        return False

c = 1
Solution().judgeSquareSum(c)