class Solution:
  def firstUniqChar(self, s: str) -> int:
    uch = []
    mp = {}
    for i,c in enumerate(s):
      mp[c] = mp.get(c, 0) + 1
      if mp[c] == 1:
        uch.append(i)
    for x in uch:
      if mp[s[x]] == 1:
        return x
    return -1

s = "leetcode"
Solution().firstUniqChar(s)