from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
      return [1]
    elif rowIndex == 1:
      return [1, 1]

    ptRow = [1, 1]
    for i in range(2, rowIndex+1):
      c = i+1
      row = [1] * c

      for j in range(1, c-1):
        row[j] = ptRow[j-1] + ptRow[j]
      ptRow = row

    return ptRow

rIndex = 30
Solution().getRow(rIndex)
