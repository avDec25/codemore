from typing import List
import heapq
import collections

class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:
    d = collections.defaultdict(list)
    
    for i,item in items:
      heapq.heappush(d[i], item)
      if len(d[i]) > 5:
        heapq.heappop(d[i])
      
      print("i: {}, heap: {}".format(i, d[i]))
      
    return [[i, sum(d[i]) // 5] for i in sorted(d)]
  
items = [[5, 91], [5, 92], [3, 93], [3, 97], [5, 60], [
    3, 77], [5, 65], [5, 87], [5, 100], [3, 100], [3, 76]]

print(Solution().highFive(items))
