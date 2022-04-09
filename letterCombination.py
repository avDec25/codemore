from curses.ascii import SO
from typing import List

class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if len(digits) == 0:
      return []
    self.mapping = {
      '2': ['a', 'b', 'c'],
      '3': ['d', 'e', 'f'],
      '4': ['g', 'h', 'i'],
      '5': ['j', 'k', 'l'],
      '6': ['m', 'n', 'o'],
      '7': ['p', 'q', 'r', 's'],
      '8': ['t', 'u', 'v'],
      '9': ['w', 'x', 'y', 'z']
    }
    self.all_combinations = []    
    self.backtrack("", digits, 0)
    return self.all_combinations

  def backtrack(self, templist, digits, start):
    if start == len(digits):
      self.all_combinations.append(templist)
    else:
      for v in self.mapping[digits[start]]:
        self.backtrack(templist + v, digits, start+1)

digits = "23"
Solution().letterCombinations(digits)
