class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans = ans ^ (start+2*i)
        return ans
        

n = 4
start = 3
Solution().xorOperation(n, start)