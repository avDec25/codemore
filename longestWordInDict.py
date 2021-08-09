from typing import List
import heapq

class Solution:
  def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    heap = [(-len(word), word) for word in dictionary]
    heapq.heapify(heap)
    while heap:
      word = heapq.heappop(heap)[1]
      it = iter(s)
      if all(c in it for c in word):
        return word
    return ''
  
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
Solution().findLongestWord(s, dictionary)
