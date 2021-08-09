import re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
      res = ""
      ints = map(int, re.findall("[+-]?\d+", expression))
      A, B = 0, 1
      for a in ints:
        b = next(ints)
        A = A*b + B*a
        B *= b
        g = math.gcd(A, B)
        A //= g
        B //= g
      return "{}/{}".format(A, B)

expression = "-1/2+1/2+1/3"
print(Solution().fractionAddition(expression))
