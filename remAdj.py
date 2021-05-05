def removeDuplicates(s: str, k: int) -> str:
  def expand(stk):
    ans = ""
    for e in stk:
      ans = ans + (e[0] * e[1])
    return ans
  
  stack = []
  n = len(s)
  stack.append([s[0], 1])
  for i in range(1, n):
    if len(stack) == 0:
      stack.append([s[i], 1])
    else:
      top = stack.pop()
      if top[0] == s[i]:
        top[1] = top[1]+1
        if top[1] < k:
          stack.append([top[0], top[1]])
      else:        
        stack.append(top)
        stack.append([s[i], 1])

  return expand(stack)


s = "abcd"
k = 3
print(removeDuplicates(s, k))
