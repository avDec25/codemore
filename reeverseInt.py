#%%
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            ans = -int(x[1:len(x):][::-1])
        else:
            ans = int(x[::-1])
        return ans if -(2**31)-1 < ans < 2**31 else 0   

x = -123
Solution().reverse(x)

# %%



