
class Solution:
    def isValid(self, s: str) -> bool:
        # follows the principal that the parenthesis which is most recently opened
        # should be closed most recently / closed first

        # Stack can maintain which bracket should be closed first, if on every open bracket we encounter
        # we insert a corresponding closed bracket

        # now if a closed bracket is encountered, we check the top of the stack
        # and this top gives the bracket which should be closed first.
        # if encountered closed bracket matches this top, means given string until now is valid
        # if does not match OR stack gets empty means InValid string of parenthesis.

        stk = []
        for char in s:
            if char == '[':
                stk.append(']')
            elif char == '(':
                stk.append(')')
            elif char == '{':
                stk.append('}')
            elif len(stk) == 0 or stk.pop() != char:
                return False

        return len(stk) == 0


s = "{(}{)}[][]({[][()]}{})"
print(Solution().isValid(s))
