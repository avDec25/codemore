# https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
  def longestDupSubstring(self, s: str) -> str:
    dp = {}
    for i in range(len(s)):
      for j in range(i+1, len(s)):
        w = s[i:j]
        print(w)
        dp[w] = dp.get(w, 0) + 1

    ans = ""
    mxVal = 0
    for key, val in dp.items():
      print(key, val)
      if mxVal < val:
        mxVal = val
        ans = key
    return ans

s = "banana"
Solution().longestDupSubstring(s)