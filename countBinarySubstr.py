def countBinarySubstr(str):
  if not str:
    return 0
  consecutiveOnes = 0
  consecutiveZeros = 0
  ans = 0
  
  for i in range(0, len(str)):
    if str[i] == '0':
      if i-1 >= 0 and str[i-1] == '1':
        consecutiveZeros = 0
      consecutiveZeros = consecutiveZeros + 1
      if consecutiveZeros <= consecutiveOnes:
        ans = ans + 1
    else:
      if i-1 >= 0 and str[i-1] == '0':
        consecutiveOnes = 0
      consecutiveOnes = consecutiveOnes + 1
      if consecutiveOnes <= consecutiveZeros:
        ans = ans + 1
  
  return ans


question = "001100011"
print(countBinarySubstr(question))
