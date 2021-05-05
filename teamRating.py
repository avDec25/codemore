from typing import List


class Solution:
  def numTeams(self, rating: List[int]) -> int:
    res = 0
    for i,c in enumerate(rating):
      llc = 0
      rgc = 0
      lgc = 0
      rlc = 0
      for l in rating[:i]:
        if l < c:
          llc += 1
        if l > c:
          lgc += 1
          
      for r in rating[i+1:]:
        if c < r:
          rgc += 1
        if c > r:
          rlc += 1
          
      res += llc * rgc + lgc * rlc
        
    return res


rating = [2, 5, 3, 4, 1]
print(Solution().numTeams(rating))
