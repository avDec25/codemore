from typing import List
from functools import cmp_to_key

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def compare(a, b):
      if a[0] == b[0]:
        return b[1] - a[1]
      return b[0] - a[0]
    ans = []
    intervals = sorted(intervals, key=cmp_to_key(compare))
    for i in range(len(intervals)-1):
      first = intervals[i]
      second = intervals[i+1]
      if overlap(first, second):
        ans.append([first[0], max(second[1], first[1])])
      
    
intervals = [[1, 3], [12, 16], [75, 80], [8, 10], [15, 18], [2, 10], [16, 21], [25, 30], [27, 29]]
Solution().merge(intervals)