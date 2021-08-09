def longestValidParentheses(x):
  stack = []
  stack.append(-1)

  ans = 0

  for i, c in enumerate(x):
    print("i:{}, c:{}".format(i,c))
    print(stack)
    print("")
    if c == '(':
      stack.append(i)
    if c == ')':
      if len(stack) != 0:
        stack.pop()
      

      if len(stack) != 0:
        top = stack[len(stack)-1]
        ans = max(ans, i-top)
      else:
        stack.append(i)
  
  print(stack)
  return ans


x = "))(())("
print(longestValidParentheses(x))
