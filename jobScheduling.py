from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0,0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1])-1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1]+p])
        return dp[-1][1]

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
Solution().jobScheduling(startTime, endTime, profit)