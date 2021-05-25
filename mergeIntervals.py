from typing import List
from functools import cmp_to_key

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def overlap(x, y):
      return x[1] >= y[0]
    
    def compare(a, b):
      if a[0] == b[0]:
        return a[1] - b[1]
      return a[0] - b[0]
    
    intervals = sorted(intervals, key=cmp_to_key(compare))
    ans = []
    ans.append(intervals[0])
    for i in range(1, len(intervals)):
      first = ans.pop()
      second = intervals[i]
      if overlap(first, second):
        minimal = min(first[0], second[0])
        maximal = max(first[1], second[1])
        ans.append([minimal, maximal])
      else:
        ans.append(first)
        ans.append(second)
    return ans

    
intervals = [[1,4],[2,3]]
Solution().merge(intervals)