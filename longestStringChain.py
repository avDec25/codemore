# https://leetcode.com/problems/longest-string-chain/
from typing import List


class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    dp = {}
    for w in sorted(words, key=len):
      print(f"w = {w}")
      for i in range(len(w)):
        print(w[:i] + w[i+1:], " = ", str(dp.get(w[:i] + w[i+1:], 0)))
      dp[w] = max( dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)) )
      print("==================")
    print(dp)
    return max(dp.values())


words = ["a","b","ba","bca","bda","bdca"]
Solution().longestStrChain(words)

