from typing import List
from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        points = sorted(map(tuple, points), key=lambda x:(x[0], x[1]))
        
        if len(points) <= 1:
            return points
        
        def cross(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (a[1]-o[1]) * (b[0]-o[0])
        
        # for lower Hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        # for upper Hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        return list(set(lower[:-1] + upper[:-1]))



points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Solution().outerTrees(points)