from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      self.all_sums = []
      candidates.sort()
      self.backtrack([], candidates, target, 0)
      return self.all_sums

    def backtrack(self, templist, candidates, sum_remain, start):
      if sum_remain < 0: return
      elif sum_remain == 0: self.all_sums.append(templist.copy())

      for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i-1]: continue
        templist.append(candidates[i])
        self.backtrack(templist, candidates, sum_remain-candidates[i], i+1)
        templist.pop()

candidates = [2, 3, 6, 7]
target = 7
Solution().combinationSum2(candidates, target)
