from typing import List
from rich.console import Console
from rich.traceback import install
from rich import print
import math
install()
console = Console()

class Solution:
    def mincostTickets(self, d: List[int], c: List[int]) -> int:
        n = len(d)
        
        dp = [math.inf] * n

        # for 1-day pass
        validity = 0
        cc = 0
        for i in range(n):
            if d[i] >= validity:
                cc += c[0]
                validity = d[i]+1
            dp[i] = min(dp[i], cc)
        print(f"After 1-day pass: {dp}")

        # for 7-day pass
        validity = 0
        cc = 0
        for i in range(n):
            if d[i] >= validity:
                cc += min(c[1], c[0])
                validity = d[i]+7
            dp[i] = min(dp[i], cc)
        print(f"After 7-day pass: {dp}")



days = [1,4,6,7,8,20]
costs = [2,7,15]
Solution().mincostTickets(days, costs)