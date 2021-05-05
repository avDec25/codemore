import sys
def brickWall(wall):
  n = len(wall)
  ans = sys.maxsize
  mp = {}
  for row in wall:
    nextEdge = 0
    rowlen = len(row)
    for i in range(0, rowlen-1):
      brick = row[i]
      nextEdge += brick
      mp[nextEdge] = mp.get(nextEdge, 0) + 1
  
  for value in mp.values():
    ans = min(ans, n - value)
  
  return ans


wall = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print(brickWall(wall))
