from typing import List
class Solution:
    def findLUSlength(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        def subsequence(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)
        for i,w in enumerate(words):
            if all(not subsequence(w, w2) for j, w2 in enumerate(words) if j!=i):
                return len(w)
        return -1

strs = ["aba","cdc","eae"]
Solution().findLUSlength(strs)