from collections import defaultdict
import heapq
import math

class Solution:
    def reachableNodes(self, edges, M, N):
        G = defaultdict(set)
        dist = [math.inf] * N
        dist[0] = 0

        for i, j, w in edges:
            G[i].add((j,w+1))
            G[j].add((j,w+1))
        
        heap = [(0,0)]

        while heap:
            min_dist, idx = heapq.heappop(heap)
            for neighbour, weight in G[idx]:
                cand = min_dist + weight
                if cand < dist[neighbour]:
                    dist[neighbour] = cand
                    heapq.heappush(heap, (cand, neighbour))
        
        ans = sum(dist[i] <= M for i in range(N))

        for i, j, w in edges:
            w1, w2 = M - dist[i], M - dist[j]
            ans += (max(0,w1) + max(0, w2))
            if w1 >= 0 and w2 >= 0:
                ans -= max(w1+w2-w, 0)

        return ans


edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
maxMoves = 10
n = 4
Solution().reachableNodes(edges, maxMoves, n)