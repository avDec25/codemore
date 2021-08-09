from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = sum(mat, [])
        if len(flat) != r*c:
            return mat
        else:
            ans = [[0 for _ in range(c)] for _ in range(r)]
            k = 0
            for i in range(r):
                for j in range(c):
                    ans[i][j] = flat[k]
                    k += 1
            return ans


matrix = [[1, 2], [3, 4]]
r = 1
c = 4
Solution().matrixReshape(matrix, r, c)