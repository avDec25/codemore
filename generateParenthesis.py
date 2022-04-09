from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    self.all_parenthesis = []
    self.lrTracking("", 0, 0, n)
    return self.all_parenthesis

  def lrTracking(self, templist, l, r, n):
    if len(templist) == n*2:
      self.all_parenthesis.append(templist)
    if l < n:
      self.lrTracking(templist + "(", l+1, r, n)
    if r < l:
      self.lrTracking(templist + ")", l, r+1, n)

n = 4
Solution().generateParenthesis(n)
