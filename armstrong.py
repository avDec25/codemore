class Solution:
  def isArmstrong(self, n: int) -> bool:
    ans = 0
    k = len(str(n))
    for d in str(n):
      d = int(d)
      ans += d**k
    return ans == n

n = 153
Solution().isArmstrong(n)
