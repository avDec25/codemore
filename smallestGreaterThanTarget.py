import bisect
from typing import List


class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]


letters = ["a","a","f","j"]
target = "a"
Solution().nextGreatestLetter(letters, target)
