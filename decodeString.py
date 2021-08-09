class Solution:
    def decodeString(self, s: str) -> str:
        stk = list()
        n = 0
        curr_str = ""
        for x in s:
            if x == '[':
                stk.append(curr_str)
                stk.append(n)
                curr_str = ""
                n = 0
            elif x == ']':
                num = stk.pop()
                prev_str = stk.pop()
                curr_str = prev_str + num * curr_str
            elif str(x).isdigit():
                n = n*10 + int(x)
            else:
                curr_str += x

        return curr_str


s = "3[a2[c]]"
Solution().decodeString(s)
