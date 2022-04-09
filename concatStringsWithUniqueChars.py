from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp:
                if a & c: continue
                else: dp.append(a | c)
        return max(len(a) for a in dp)

arr = ["cha","r","act","ers"]
Solution().maxLength(arr)