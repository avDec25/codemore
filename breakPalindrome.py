class Solution:
    def breakPalindrome(self, a: str) -> str:
        for i in range(len(a)//2):
            if a[i] != 'a':
                return a[:i] + 'a' + a[i+1:]
        return a[:-1] + 'b' if a[:-1] else ''

palindrome = "aaaaa"
Solution().breakPalindrome(palindrome)