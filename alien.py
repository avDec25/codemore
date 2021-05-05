def isAlienSorted(words, order):
  index = 0
  mapOrder = {}
  for x in order:
    mapOrder[x] = index
    index = index + 1
    
  print(mapOrder)
    
  for i in range(0, len(words)-1):
    for j in range(i+1, len(words)):
      x = words[i]
      y = words[i+1]
      mnLen = min(len(x), len(y))
      k = 0
      while k < mnLen:
        if mapOrder[x[k]] > mapOrder[y[k]]:
          print("failed at x: {}, y: {}, k: {}".format(x, y, k))
          return False
        elif mapOrder[x[k]] < mapOrder[y[k]]:
          break
        k = k + 1
      if mnLen == k:
        if len(x) > len(y):
          return False
  
  return True


words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
# words = ["hello", 
#          "leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))
