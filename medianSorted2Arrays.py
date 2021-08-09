import math

def findMedianSortedArrays(x, y) -> float:
  nx = len(x)
  ny = len(y)

  if nx > ny:
    return findMedianSortedArrays(y, x)
  
  start = 0
  end = nx

  while start <= end:
    px = (start+end) // 2
    py = (nx+ny+1) // 2 - px

    mxLeftX = -math.inf if px == 0 else x[px-1]
    mxLeftY = -math.inf if py == 0 else y[py-1]

    mnRightX = math.inf if px == nx else x[px]
    mnRightY = math.inf if py == ny else y[py]

    if mxLeftX <= mnRightY and mxLeftY <= mnRightX:
      if (nx+ny)%2 == 0:
        return (max(mxLeftX, mxLeftY) + min(mnRightX, mnRightY)) / 2
      else:
        return max(mxLeftX, mxLeftY)
    elif mxLeftX > mnRightY:  # mxLeftX should have been small but we found it big, \
      end = px - 1            # hence px correct value where the expected condition happens will be found in left part
    else:
      start = px + 1
    

a = [3, 7, 9, 15, 18, 21, 25]
b = [4, 6, 8, 10, 11, 18]

# a = [23, 26, 31, 35]
# b = [3, 5, 7, 9, 11, 16]

print(findMedianSortedArrays(a, b))
