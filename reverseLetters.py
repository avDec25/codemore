import string

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = string.ascii_lowercase + string.ascii_uppercase        
        def findNextCh():
            for ch in s[::-1]:
                if ch in letters:
                    yield ch

        s_copy = [ch for ch in s]
        n = len(s_copy)
        
        gen = findNextCh()
        for k in range(n):
            if s_copy[k] in letters:
                s_copy[k] = next(gen)
        
        return ''.join(s_copy)

s = "Test1ng-Leet=code-Q!"
Solution().reverseOnlyLetters(s)