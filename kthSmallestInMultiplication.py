from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
import heapq


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # check if candidate is enough to have 
        # atleast k smaller numbers than it
        
        def feasible(enough):
            count = 0
            for v in range(1, m+1):
                add = min(n, enough // v)
                if add == 0:
                    break
                count += add
            return count >= k

        left, right = 1, m*n
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1                
        return left


m = 9895
n = 28405
k = 100787757
Solution().findKthNumber(m, n, k)
