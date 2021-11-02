from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()

from typing import List
import collections

class Solution:
    def canReorderDoubled(self, a: List[int]) -> bool:
        counter = collections.Counter(a)
        for c in sorted(counter, key=abs):
            if counter[c] > counter[2*c]:
                return False
            counter[2*c] -= counter[c]
        return True

arr = [1,2,4,16,8,4]
Solution().canReorderDoubled(arr)