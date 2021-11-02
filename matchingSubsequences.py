from collections import defaultdict
from typing import List

class Solution:
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    waiting = defaultdict(list)
    for it in map(iter, words):
      waiting[next(it)].append(it)
    
    for c in s:
      for it in waiting.pop(c, ()):
        waiting[next(it, None)].append(it)

    return len(waiting[None])

s = "abcde"
words = ["aa","bb","cde", "xy", "a", "b"]
print(Solution().numMatchingSubseq(s, words))