from typing import List

class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:    
    self.all_combinations = []
    self.backtrack([], k, n, 1)
    return self.all_combinations
    
  def backtrack(self, templist, elements, sum_remain, start):
    if sum_remain < 0 and elements < 0: return
    
    if elements == 0 and sum_remain == 0:
      self.all_combinations.append(templist.copy())

    for i in range(start, 10):
      templist.append(i)
      self.backtrack(templist, elements-1, sum_remain-i, i+1)
      templist.pop()

k = 3
n = 9
print(Solution().combinationSum3(k, n))