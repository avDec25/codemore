from typing import List

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    nr = len(matrix)
    nc = len(matrix[0])

    l, r = 0, nr*nc-1
    while l <= r:
      m = (r+l)//2
      middle = matrix[m//nc][m%nc]
      if target == middle: return True
      if target < middle:
        r = m-1
      else:
        l = m+1

    return -1
