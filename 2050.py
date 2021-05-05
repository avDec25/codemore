def numDigits(n):
  return len(str(n))

def compute2050(num):
  if num < 2050:
    return -1
  
  if num == 2050:
    return 1
  
  ans = 0
  while num > 0:
    k = numDigits(num) - 4
    divisor = 2050 * pow(10, k)
    while divisor > num:
      k = k - 1
      divisor = 2050 * pow(10, k)
    whole = num // divisor
    ans += whole
    num = num - (whole * divisor)
    if whole == 0:
      break
  
  return ans

n = int(input())
while n > 0:
  x = int(input())
  print(compute2050(x))
  n = n - 1
