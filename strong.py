t = int(input())
while t > 0:
  n, k = (int(x) for x in input().split())
  s = input()
  found = False
  cpk = 0
  for x in range(0, n):
    if s[x] == '*':
      for i in range(x, n):
        if s[i] == '*':
          cpk = cpk + 1
          if cpk == k:
            break
        else:
          break
    if cpk >= k:
      found = True
      break
    else:
      x = x + cpk
      cpk = 0
      
      
  if found:
    print("YES")
  else:
    print("NO")
  t = t - 1
