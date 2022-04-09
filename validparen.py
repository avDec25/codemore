#%%
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for ch in s:
            if ch == '(':
                brackets.append('(')
            elif ch == '{':
                brackets.append('{')
            elif ch == '[':
                brackets.append('[')

            elif ch == ')':
                if len(brackets) == 0: return False
                if brackets[-1] != '(': return False
                brackets.pop()
            elif ch == '}':
                if len(brackets) == 0: return False
                if brackets[-1] != '{': return False
                brackets.pop()
            elif ch == ']':
                if len(brackets) == 0: return False
                if brackets[-1] != '[': return False
                brackets.pop()

        if len(brackets) != 0:
            return False

        return True

s = "[()[({)]}({]}([)(])})"
Solution().isValid(s)
# %%
