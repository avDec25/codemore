from typing import List
import collections

class Solution:
  def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
    ans = []
    codex = collections.defaultdict()
    
    def translate(c):      
      if c not in codex:
        codex[c] = chr(len(codex) + 97)
      return codex[c]

    def compare(word):
      codex.clear()
      for i in range(len(word)):
        if translate(word[i]) != cipher[i]:
          return False
      return True

    cipher = [translate(c) for c in pattern]
    for word in words:
      if compare(word):
        ans.append(word)
    return ans
    

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "xyy"
Solution().findAndReplacePattern(words, pattern)
