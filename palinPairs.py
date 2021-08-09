from typing import List


class Solution:
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    def isPalindrome(w):
      return w == w[::-1]

    ans = list()
    words = {word: i for i, word in enumerate(words)}
    for word, k in words.items():
      n = len(word)
      for j in range(n+1):
        prefix = word[:j]
        suffix = word[j:]

        if isPalindrome(prefix):
          back = suffix[::-1]
          if back != word and back in words:
            ans.append([words[back], k])

        if j != n and isPalindrome(suffix):
          back = prefix[::-1]
          if back != word and back in words:
            ans.append([k, words[back]])


    return ans

words = ["a",""]
Solution().palindromePairs(words)