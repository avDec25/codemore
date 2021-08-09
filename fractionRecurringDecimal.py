class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    q, r = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator * denominator < 0 else ''
    integer = sign + str(q)
    
    if r == 0:
      return integer
    
    decimal = ''
    i = 0
    rs = {}
    while r > 0 and r not in rs:
      rs[r] = i
      q, r = divmod(r*10, abs(denominator))
      decimal += str(q)
      i += 1
    
    if r in rs:
      i = rs[r]
      return integer + '.' + decimal[:i] + '(' + decimal[i:] + ')'
    else:
      return integer + '.' + decimal[:]

numerator = 1
denominator = 6
Solution().fractionToDecimal(numerator, denominator)
