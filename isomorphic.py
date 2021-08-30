# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = dict()
        mt = dict()
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in ms and ms[s[i]] != t[i]: return False
                if t[i] in mt and ms[t[i]] != s[i]: return False
                ms[s[i]] = t[i]
                mt[t[i]] = s[i]
            return True
        else:
            return False


s = "badc"
t = "baba"
Solution().isIsomorphic(s, t)