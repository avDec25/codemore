#%%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        print(s)
        return s == s[::-1]

s = "A man, a plan, a canal: Panama"
s = "0P"
Solution().isPalindrome(s)

# %%
