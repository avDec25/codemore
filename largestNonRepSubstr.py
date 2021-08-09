def largestNonRepSubStr(s):
  seen = {}
  
  start = 0
  mxlen = 0

  for end,x in enumerate(s):
    if x in seen:
      start = max(start, seen[x]+1)
    seen[x] = end
    mxlen = max(mxlen, end-start+1)

  return mxlen

s = "GWzcxWGAkzQwtRV"
print(largestNonRepSubStr(s))
