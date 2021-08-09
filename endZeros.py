def end_zeros(num: int) -> int:
  data = str(num)
  ans = 0
  for ch in reversed(data):
    if ch != '0':
      break
    else:
      ans += 1
  return ans

print(end_zeros(10100))