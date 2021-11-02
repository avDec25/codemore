from rich.console import Console
from rich.traceback import install
from rich import inspect
install()
console = Console()

class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        e0 = 1
        e1 = 0
        e2 = 0
        # inspect(s)
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0')*e0 + e1 + (c <= '6')*e2
                f1 = (c == '1')*e0
                f2 = (c == '2')*e0
            # console.log(log_locals=True)
            e0, e1, e2 = f0 % MOD, f1, f2
        
        return e0


s = "06"
Solution().numDecodings(s)
