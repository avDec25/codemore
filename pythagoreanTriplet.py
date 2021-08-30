from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()

from typing import List
import bisect

class Solution:
    def triangleNumber(self, a: List[int]) -> int:
        n = len(a)
        a.sort()
        for i in range(n):
            for j in range(i+1, n):
                print(f"searched for = {a[i]+a[j]}")
                index = bisect.bisect_left(a, a[i]+a[j]+1)
                print(f"count = {n - index}")
                console.log(log_locals=True)


nums = [2, 2, 3, 4]
Solution().triangleNumber(nums)
