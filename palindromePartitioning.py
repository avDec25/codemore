from typing import List


class Solution:
  def partition(self, s: str) -> List[List[str]]:
    self.all_palindromes = []
    self.backtrack([], s, 0)
    return self.all_palindromes
  
  def backtrack(self, templist, s, start):
    if start == len(s):
      self.all_palindromes.append(templist.copy())
    else:
      for i in range(start, len(s)):
        if self.is_palindrome(s, start, i):    # check if a substring is is_palindrome
          templist.append(s[start:i+1])        # because it is one, add it to templist
          self.backtrack(templist, s, i+1)     # start from the next character in s
          templist.pop()

  def is_palindrome(self, s, low, high):
    while low < high:
      if s[low] != s[high]:
        return False
      low += 1
      high -= 1
    return True

s = "aab"
print(Solution().partition(s))