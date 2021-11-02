from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
from typing import List

class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        H = len(a)
        W = len(a[0])
        zr = set()
        zc = set()
        for i in range(H):
            for j in range(W):
                if a[i][j] == 0:
                    zr.add(i)
                    zc.add(j)
        
        for i in range(H):
            for j in range(W):
                if i in zr or j in zc:
                    a[i][j] = 0


matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)