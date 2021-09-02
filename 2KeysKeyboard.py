from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        i = 2
        while i <= n:
            dp[i] = i

            # start from i-1 all the way upto 1
            j = i-1
            while j > 1:
                # if we find a factor, then operations to create that factor
                # plus i//j; i.e. number of times that factor can make i
                if i % j == 0:
                    dp[i] = dp[j] + (i//j)
                    break
                j -= 1
            i += 1
        print(dp)
        return dp[n]

n = 12
Solution().minSteps(n)