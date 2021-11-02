from rich.console import Console
from rich.traceback import install
from rich import inspect
install()
console = Console()

class Solution:
    def numDecodings(self, s: str) -> int:
        e0 = 1
        e1 = 0
        e2 = 0
        inspect(s)
        for c in s:
            print("======================")
            print(f"c={c}")
            print(f"e0={e0}, e1={e1}, e2={e2}")
            f0 = (c  > '0')*e0 + e1 + (c <= '6')*e2
            f1 = (c == '1')*e0
            f2 = (c == '2')*e0
            e0, e1, e2 = f0, f1, f2
            print(f"e0={e0}, e1={e1}, e2={e2}")
        
        return e0


s = "127"
Solution().numDecodings(s)
