class Solution:
    def reviveKill(self, a):
        m = len(a)
        n = len(a[0])

        ans = [[a[i][j] for j in range(n)] for i in range(m)]
        
        def safe(i, j):
            return 0 <= i < m and 0 <= j < n

        def newVal(i, j):
            live = 0
            dead = 0
            for dx, dy in [(-1,0), (0,-1), (-1,-1), (1,0), (0,1), (1,1), (-1, 1), (1, -1)]:
                x = dx + i
                y = dy + j
                if safe(x, y):
                    if a[x][y] == 1: live += 1
                    if a[x][y] == 0: dead += 1
            
            if a[i][j] == 1:
                if live < 2: return 0
                if live > 3: return 0
            if a[i][j] == 0:
                if live == 3: return 1
            return a[i][j]

        for i in range(m):
            for j in range(n):
                ans[i][j] = newVal(i, j)
        return ans


matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
Solution().reviveKill(matrix)
