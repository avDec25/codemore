from typing import List
import collections

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    ans = 0
    deadends = set(deadends)
    q = collections.deque(["0000"])
    seen = set("0000")

    while q:
      size = len(q)         # this is done to prevent that Marker element insertion in queue
      for _ in range(size): # which was done in cpp code for queue
        cand = q.popleft()
        
        if cand in deadends:
          continue
        
        if cand == target:
          return ans
        
        temp = cand
        for k in range(4):
          currPos = int(temp[k])
          c1 = temp[0:k] + ( '0' if currPos == '9' else str((currPos+1)%10) ) + temp[k+1:]
          c2 = temp[0:k] + ( '9' if currPos == '0' else str((currPos-1)%10) ) + temp[k+1:]

          if c1 not in seen and c1 not in deadends:
            seen.add(c1)
            q.append(c1)

          if c2 not in seen and c2 not in deadends:
            seen.add(c2)
            q.append(c2)
      ans += 1
    return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
Solution().openLock(deadends, target)