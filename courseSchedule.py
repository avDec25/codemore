#%%
def canFinish(n, prerequisites):
    G = [[] for i in range(n)]
    degree = [0] * n
    for j, i in prerequisites:
        G[i].append(j)
        degree[j] += 1

    # print(f"bfs = {bfs}")

    bfs = [i for i in range(n) if degree[i] == 0]
    print(f"bfs = {bfs}")

    for i in bfs:
        for j in G[i]:
            degree[j] -= 1
            if degree[j] == 0:
                bfs.append(j)
    return len(bfs) == n

numCourses = 5
prerequisites = [[1,0],[2,1],[3,1],[4,2],[3,4]]
canFinish(numCourses, prerequisites)

# %%
