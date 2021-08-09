class Solution:
    def mySqrt(self, x: int) -> int:
        def condition(i):
            return i*i > x

        left, right = 0, x+1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid+1
        return left-1
        
x = 8
Solution().mySqrt(x)
