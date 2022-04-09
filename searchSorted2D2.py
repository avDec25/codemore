from typing import List
import bisect

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    nc = len(matrix[0])
    
    for row in matrix:
      if row[0] <= target <= row[-1]:
        index = bisect.bisect_left(row, target)
        if index == nc: continue
        if row[index] == target: return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
Solution().searchMatrix(matrix, target)