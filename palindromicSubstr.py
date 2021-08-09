class Solution:
  def countSubstrings(self, s: str) -> int:
    if s is None or len(s) == 0:
      return 0
    
    n = len(s)
    ans = 0
    
    def extendPalin(s, left, right):
      count = 0
      while 0 <= left < n and 0 <= right < n and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
      return count
    
    for i in range(n):
      ans += extendPalin(s, i, i);
      ans += extendPalin(s, i, i+1);
    
    return ans


s = "abc"
Solution().countSubstrings(s)
