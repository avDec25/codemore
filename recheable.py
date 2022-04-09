from typing import List
from collections import defaultdict
import heapq

class Solution:
    def reachableNodes(self, edges, M, N):
        e = defaultdict(dict)
        for i, j, l in edges: e[i][j] = e[j][i] = l
        pq = [(-M, 0)]
        seen = {}
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in e[i]:
                    moves2 = -moves - e[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))
        res = len(seen)
        for i, j, _ in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), e[i][j])
        return res

edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
maxMoves = 10
n = 4
Solution().reachableNodes(edges, maxMoves, n)