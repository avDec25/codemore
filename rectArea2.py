from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        area = 0
        # MOD = 10**9+7
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        print(xs)
        return area

rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Solution().rectangleArea(rectangles)