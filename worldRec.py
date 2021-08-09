import math

T = int(input())
while T > 0:
  k1, k2, k3, v = (round(float(x), 2) for x in input().split())
  fspeed = k1*k2*k3*v
  tt = round(100/fspeed, 2)
  if tt < 9.58:
    print("YES")
  else:
    print("NO")
  T = T - 1
