class Solution:
  def judgeCircle(self, moves: str) -> bool:
    x = 0
    y = 0
    for move in moves:
      if move == 'U': x, y = x, y+1
      if move == 'D': x, y = x, y-1
      if move == 'L': x, y = x-1, y
      if move == 'R': x, y = x+1, y+1
    return (x == 0 and y == 0)
  
moves = "LDRRLRUULR"
Solution().judgeCircle(moves)
