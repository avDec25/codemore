sol = []
def _generate(ans, n, pos, openP, closeP):
  if closeP == n:    
    sol.append("".join(ans))
  
  else:
    if openP > closeP:  # this will cause to put open paren first before placing a closed one
      ans[pos] = ")"
      _generate(ans, n, pos+1, openP, closeP+1)

    if openP < n:
      ans[pos] = "("
      _generate(ans, n, pos+1, openP+1, closeP)


def generateAll(n):
  ans = [''] * 2 * n
  _generate(ans, n, 0, 0, 0)
  

n = 2
generateAll(n)
print(sol)
