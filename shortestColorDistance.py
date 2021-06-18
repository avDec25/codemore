from typing import List
import bisect
import collections
import math

class Solution:
  def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
    ans = []
    cIndex = collections.defaultdict(list)
    for i, c in enumerate(colors):
      cIndex[c].append(i)
    
    for q in queries:
      i, c = q[0], q[1]
      if c not in cIndex:
        ans.append(-1)
        continue
      else:
        c1 = bisect.bisect_left(cIndex[c], i)
        n = len(cIndex[c])
        if c1 >= n:
          c1 = n-1
        ans.append(min([abs(cIndex[c][c1]-i), abs(cIndex[c][c1-1]-i) if (c1-1 >= 0) else math.inf]))

    return ans

# colors =[1,1,2,1,3,2,2,3,3]
# queries =[[1,3],[2,2],[6,1]]

colors = [2,1,2,2,1]
queries = [[1,1],[4,3],[1,3],[4,2],[2,1]]

Solution().shortestDistanceColor(colors, queries)
