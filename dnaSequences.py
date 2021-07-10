# https://leetcode.com/problems/repeated-dna-sequences/
from typing import List

class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    sequences = set()
    ans = set()
    for i in range(len(s)-10+1):
      seq = s[i:i+10]
      if seq in sequences:
        ans.add(seq)
      else:
        sequences.add(seq)
    return list(ans)


s = "AAAAAAAAAAA"
Solution().findRepeatedDnaSequences(s)