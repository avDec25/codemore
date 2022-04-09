from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      self.all_sums = []
      candidates.sort()
      self.backtrack([], candidates, target, 0)
      return self.all_sums

    def backtrack(self, templist, candidates, sum_remain, start):
      if sum_remain < 0: return
      elif sum_remain == 0: self.all_sums.append(templist.copy())

      for i in range(start, len(candidates)):
        templist.append(candidates[i])
        # i because we can resue same element unlimited number of times
        self.backtrack(templist, candidates, sum_remain-candidates[i], i)
        templist.pop()

candidates = [2, 3, 6, 7]
target = 7
Solution().combinationSum(candidates, target)
      