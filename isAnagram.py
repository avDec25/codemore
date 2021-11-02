from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = dict()
        for x in s:
            setS[x] = setS.get(x, 0) + 1
        
        setT = dict()
        for x in t:
            setT[x] = setT.get(x, 0) + 1
        
        return setS == setT
        
s = "anagram"
t = "nagaram"
Solution().isAnagram(s, t)