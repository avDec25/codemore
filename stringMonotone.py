from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()

class Solution:    
    def minFlipsMonoIncr(self, s: str) -> int:
        flip = 0
        c1 = 0
        for x in s:
            if x == '1':
                c1 += 1
            else:
                flip += 1
            flip = min(flip, c1)
        return flip


s = "0000101000110"
Solution().minFlipsMonoIncr(s)