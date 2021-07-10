from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 1:
      return [[1]]
    pascalsTriangle = [[1], [1, 1]]

    for i in range(2, numRows):
      c = i+1
      row = [1] * c
      for j in range(1, c-1):
        row[j] = pascalsTriangle[i-1][j-1] + pascalsTriangle[i-1][j]
      pascalsTriangle.append(row)


    return pascalsTriangle

numRows = 1
Solution().generate(numRows)