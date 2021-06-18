from typing import List

class Solution:
  def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
    covered = dict()

    for r in ranges:
      for x in range(r[0], r[1]+1):
        covered[x] = True

    for i in range(left, right+1):
      if covered.get(i, False) == False:
        return False

    return True

ranges = [[1,10],[10,20]]
left = 21
right = 21
Solution().isCovered(ranges, left, right)