from typing import List

class Solution:
  def makesquare(self, matchsticks: List[int]) -> bool:

    def dfs(stickIndex, t):
      if stickIndex == len(matchsticks):
        return True

      for i in range(4):
        if t[i] >= matchsticks[stickIndex]:
          t[i] -= matchsticks[stickIndex] # try with this current stick
          if dfs(stickIndex+1, t):
            return True
          target[i] += matchsticks[stickIndex] # undo the change
        
      return False

    if len(matchsticks) < 4:
      return False

    lenSum = sum(matchsticks)
    if lenSum % 4 != 0:
      return False

    # matchsticks.sort(reverse=True)
    target = [lenSum/4] * 4
    print(f'**************{target}**************')

    return dfs(0, target)


matchsticks = [1,1,2,2,2]
Solution().makesquare(matchsticks)