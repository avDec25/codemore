from string import ascii_lowercase

class Solution:
  def rabinKarp(self, s, pat):
    cipher = {ch: i+1 for i, ch in enumerate(ascii_lowercase)}

    n = len(pat)
    def computeHash(p) -> int:
      return sum(cipher[x] * pow(10, n-i-1) for i,x in enumerate(p))

    patHash = computeHash(pat)
    currHash = computeHash(s[:n])

    for i in range(1, len(s)-n+1):
      currHash = (currHash - cipher[s[i-1]]*pow(10,n-1)) * 10 + cipher[s[i+n-1]]
      if currHash == patHash and pat == s[i:i+n]:
        return True

    return False

s = "ccaccaaedba"
pat = "dba"
Solution().rabinKarp(s, pat)
