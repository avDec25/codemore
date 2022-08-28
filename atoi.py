#%%
class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1
        if len(s) == 0:
            return 0
        
        while pos < len(s):
            cc = s[pos]
            if state == 0:
                if cc == " ":
                    state = 0
                elif cc == "+" or cc == "-":
                    state = 1
                    sign = [1, -1][cc == "-"]
                elif cc.isdigit():
                    state = 2
                    value = value * 10 + int(cc)
                else:
                    return 0
            elif state == 1:
                if cc.isdigit():
                    state = 2
                    value = value*10 + int(cc)
                else:
                    return 0
            elif state == 2:
                if cc.isdigit():
                    state = 2
                    value = value*10 + int(cc)
                else:
                    break
            else:
                return 0
            pos += 1
        value = sign * value
        value = min(value, 2**31 -1 )
        value = max(value, -(2**31))
        return value
    
s = "42" 
Solution().myAtoi(s)
# %%
