from typing import List

class Solution:
  def chalkReplacer(self, chalk: List[int], k: int) -> int:
    n = len(chalk)
    i = 0
    k = k % sum(chalk)
    while k > 0:
      if k < chalk[i]:
        return i
      k -= chalk[i]
      i = (i+1) % n
    return i


chalk = [3,4,1,2]
k = 25
Solution().chalkReplacer(chalk, k)
