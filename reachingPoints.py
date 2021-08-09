class Solution:
  def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    while tx >= sx and ty >= sy:
      if tx > ty:
        if sy == ty: return (tx-sx) % ty == 0
        tx %= ty
      else:
        if sx == tx:
          # if all from ty removed after sy then after remove all of tx from that, 
          # remainder should be zero
          return (ty-sy) % tx == 0
        # remove all that was added of tx from ty
        ty %= tx
    return False

sx = 1
sy = 1
tx = 3
ty = 5
print(Solution().reachingPoints(sx, sy, tx, ty))
