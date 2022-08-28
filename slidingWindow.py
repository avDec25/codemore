# %%
# Substrings of Size Three with Distinct Characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n+1-3):
            a, b, c = s[i:i+3]
            if a!=b and b!=c and c!=a:
                result += 1
        return result

s = "aababcabc"
s = "xyzzaz"
Solution().countGoodSubstrings(s)

# %%
# Longest Nice Substring
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ""
        ss = set(s)
        for i, c in enumerate(s):
            # cut the string into two if character swapped case is
            # not in the set of characters within the provided string
            # meaning the substring will be either in the left substring
            # or the right substring
            if c.swapcase() not in ss:
                sl = self.longestNiceSubstring(s[:i])
                sr = self.longestNiceSubstring(s[i+1:])
                return max(sl, sr, key=len)
        return s

s = "YazaAay"
Solution().longestNiceSubstring(s)

# %%
# Longest Substring with k Distinct Characters
class Solution:
    def longestKSubstr(self, s, k) -> int:
        freq = {}
        l, r = 0, 0
        result = 0
        for i in range(len(s)):
            r = i
            freq[s[i]] = freq.get(s[i], 0) + 1
            print(freq)
            while l<=r and len(freq) > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1
                if freq[s[l]] == 0:
                    freq.pop(s[l])
            result = max(result, len(freq))
        print(s[l:r+1])
        return result

s = "aabacbebebe"
k = 2
Solution().longestKSubstr(s, k)
# %%
