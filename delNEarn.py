from typing import List
import collections


class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    points, prev, curr = collections.Counter(nums), 0, 0
    print(points)
    for value in range(10001):
      prev, curr = curr, max(prev + value * points[value], curr)
    return curr


nums = [3, 4, 2, 2, 1, 1, 3, 3, 3, 3, 5]
print(Solution().deleteAndEarn(nums))
