from typing import List
from scipy.spatial import ConvexHull
import numpy as np

class Solution:
    def outerTrees(self, points):
        def isHull(point, hull, tol=1e-12):
            return any((abs(np.dot(eq[:-1], point) + eq[-1]) < tol) for eq in hull.equations)
        try:
            hull = ConvexHull([(p.x, p.y) for p in points])
            return [p for p in points if isHull((p.x, p.y), hull)]
        except:
            return points

points = [[1,2],[2,2],[4,2]]
Solution().outerTrees(points)