from typing import List
from functools import cmp_to_key

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def compare(a, b):
      if a[0] == b[0]:
        return a[1] - b[1]
      else:
        return a[0] - b[0]
    
    def overlaps(a, b):
      return a[1] >= b[0]

    intervals = sorted(intervals, key=cmp_to_key(compare))
    ans = list()
    ans.append(intervals[0])
    for i in range(1, len(intervals)):
      first = ans.pop()
      second = intervals[i]
      if overlaps(first, second):
        minimal = min(first[0], second[0])
        maximal = max(first[1], second[1])
        ans.append([minimal, maximal])
      else:
        ans.append(first)
        ans.append(second)
    
    return ans



intervals = [[1,3],[2,6],[8,10],[15,18]]
Solution().merge(intervals)