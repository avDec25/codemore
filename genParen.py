from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    def generate(p, left, right, ans=[]):
      if left:
        # n return here, means continue to append
        generate(p+'(', left-1, right)
      if right > left:
        generate(p+')', left, right-1)      
      
      if not right:
        ans += [p]
        # can also be replaced by this comma thing:
        # ans += p,
        print(f'ans = {ans}')
        print(f'================================================================')
      return ans

    return generate('', n, n)


n = 3
Solution().generateParenthesis(n)
