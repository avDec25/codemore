from typing import List

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        r = len(a)
        c = len(a[0])
        res = []

        up, down = 0, r-1
        left, right = 0, c-1
        while len(res) < r*c:
            j = left
            while j <= right and len(res) < r*c:
                res.append(a[up][j])
                j += 1
            
            i = up + 1
            while i <= down-1 and len(res) < r*c:
                res.append(a[i][right])
                i += 1
            
            j = right
            while j >= left and len(res) < r*c:
                res.append(a[down][j])
                j -= 1
            
            i = down-1
            while i >= up+1 and len(res) < r*c:
                res.append(a[i][left])
                i -= 1

            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res
        
a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
Solution().spiralOrder(a)
