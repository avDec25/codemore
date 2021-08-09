class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int1 = [int(i) for i in reversed(num1)]
        int2 = [int(i) for i in reversed(num2)]
        carry = 0
        ans = []
        i = 0
        while i < min(len(int1), len(int2)):
            sm = (int1[i] + int2[i] + carry)            
            carry = sm//10
            ans.append(
                sm%10
            )
            i += 1
        if i == len(int1):
            for j in range(i, len(int2)):
                sm = int2[j] + carry
                carry = sm // 10
                ans.append(
                    sm % 10
                )
        elif i == len(int2):
            for j in range(i, len(int1)):
                sm = int1[j] + carry
                carry = sm // 10
                ans.append(
                    sm % 10
                )
        if carry > 0:
            ans.append(carry)
        ans = [str(i) for i in reversed(ans)]
        return ''.join(ans)

num1 = "11"
num2 = "123"
Solution().addStrings(num1, num2)