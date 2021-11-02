class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 and high & 1:
            return (high-low)//2+1
        elif low % 2 == 0 and high % 2 == 0:
            return (high-low)//2
        else:
            return (high-low+1)//2

low = 8
high = 10
Solution().countOdds(low, high)