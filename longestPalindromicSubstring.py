# Longest Palindromic Substring
from functools import lru_cache


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while 0 <= l <= r and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        ans = ""
        for i in range(len(s)):
            odd = palindrome(s, i, i)
            even = palindrome(s, i, i+1)
            ans = max(ans, odd, even, key=len)
        return ans


s = "holaamarramahello"
Solution().longestPalindrome(s)
