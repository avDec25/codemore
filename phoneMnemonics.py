from collections import deque

mapping = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z']
}

def mnemonics(s):
  n = len(s)
  list = []
  q = deque()
  q.append("")
  
  while len(q) != 0:
    popped = q.pop()
    if len(popped) == n:
      list.append(popped)
    else:
      for letter in mapping[s[len(popped)]]:
        q.append(popped + letter)
        
  return list
    
digits = "92"
print(mnemonics(digits))
