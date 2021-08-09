from typing import List


class Solution:
  def compress(self, chars: List[str]) -> int:
    ans, i = 0, 0
    while i < len(chars):
      curr = chars[i]
      count = 0
      while i < len(chars) and chars[i] == curr:
        count += 1
        i += 1
      chars[ans] = curr
      ans += 1
      if count != 1:
        for c in str(count):
          chars[ans] = c
          ans += 1
    return ans


chars = ["a", "a", "b", "b", "c", "c", "c"]
Solution().compress(chars)