import collections
class Solution:
  def largestOddNumber(self, num: str) -> str:
    for x in range(len(num)-1, -1, -1):
      print(num[x])
      if int(num[x]) % 2 != 0:
        return num[:x+1]
    return ""

num = "12454683121"
Solution().largestOddNumber(num)