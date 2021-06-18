from typing import List
import collections

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    ans = 0
    deadends = set(deadends)
    seen = set("0000")
    q = collections.deque(['0000'])
    while q:
      size = len(q)
      for _ in range(size):
        cand = q.popleft()
        if cand == target:
          return ans
        if cand in deadends:
          continue
        temp = cand
        for i in range(4):
          cc = int(temp[i])
          c1 = temp[0:i] + ('0' if cc == '9' else str((cc+1)%10) ) + temp[i+1:]
          c2 = temp[0:i] + ('9' if cc == '0' else str((cc-1)%10) ) + temp[i+1:]
          if c1 not in seen and c1 not in deadends:
            seen.add(c1)
            q.append(c1)
          if c2 not in seen and c2 not in deadends:
            seen.add(c2)
            q.append(c2)
      ans += 1  

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
Solution().openLock(deadends, target)