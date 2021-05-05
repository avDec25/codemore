from typing import List


class Solution:
  def lastRemaining(self, n: int) -> int:
    l2r, head, remains, step = True, 1, n, 1
    while remains > 1:
      if l2r or remains % 2 ==1:
        head += step
        
      remains = remains // 2
      step *= 2
      l2r = not l2r
    return head


n = 9
print(Solution().lastRemaining(n))
