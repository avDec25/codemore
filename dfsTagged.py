#%%
# Invert Binary Tree
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def preOrder(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       if root:
           root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
           return root

    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root
    
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = deque([root])
        while stk:
            node = stk.pop()
            if node:
                node.left, node.right = node.right, node.left
                stk.append(node.left) if node.left is not None else "pass"
                stk.append(node.right) if node.right is not None else "pass"
            print(stk)
        return root

rl = TreeNode(6)
rr = TreeNode(9)
ll = TreeNode(1)
lr = TreeNode(3)
l = TreeNode(2, ll, lr)
r = TreeNode(7, rl, rr)
root = TreeNode(4, l, r)

Solution().preOrder(root)
print("==================")
Solution().invertTreeDFS(root)
print("==================")
Solution().preOrder(root)

# %%
# Diameter of Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.depth(root)
        return self.dia
    
    def depth(self, root: Optional[TreeNode]) -> int:
        if root:
            ld = self.depth(root.left)
            rd = self.depth(root.right)
            self.dia = max(ld+rd, self.dia)
            return 1+max(ld, rd)
        else:
            return 0

# rl = TreeNode(6)
rr = TreeNode(6)
ll = TreeNode(3)
lr = TreeNode(4)
l = TreeNode(2, ll, lr)
r = TreeNode(5, None, rr)
root = TreeNode(1, l, r)
Solution().diameterOfBinaryTree(root)

#%%
# Flatten Binary Tree to Linked List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
            
    def preOrder(self, root: Optional[TreeNode]) -> None:
        if root:
            print(root)
            self.preOrder(root.left)
            self.preOrder(root.right)

rr = TreeNode(6)
ll = TreeNode(3)
lr = TreeNode(4)
l = TreeNode(2, ll, lr)
r = TreeNode(5, None, rr)
root = TreeNode(1, l, r)
Solution().flatten(root)
Solution().preOrder(root)


# %%
# Course Schedule
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = dict()
        for i in range(numCourses):
            adjList[i] = set()

        for edge in prerequisites:
            u, v = edge
            adjList[v].add(u)

        for v in adjList.keys():
            print(f"{v}: {adjList[v]}")

        visited = [0 for _ in range(numCourses)]
        for node in range(numCourses):
            if self.dfsForCycle(adjList, visited, node):
                return False
        return True

    # return true if cycle is found
    def dfsForCycle(self, adj_list, visited, node) -> bool:
        # means node is being visited and is got back to at again
        # hence it a cycle
        if visited[node] == -1:
            return True
        
        # already visited, not required to visit again
        if visited[node] == 1:
            return False
        
        visited[node] = -1
        for neighbour in adj_list[node]:
            if self.dfsForCycle(adj_list, visited, neighbour):
                return True
        visited[node] = 1
        return False

numCourses = 8
prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
Solution().canFinish(numCourses, prerequisites)
# %%
# Topological Sort
from typing import List
from collections import deque

class Solution:
    def generate_adj_list(self, num_courses, edge_list):
        adjList = dict()
        for i in range(num_courses):
            adjList[i] = set()

        for edge in edge_list:
            u, v = edge
            adjList[v].add(u)

        return adjList

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.topo_bfs(numCourses, prerequisites)

    def topo_bfs(self, V: int, E: dict) -> bool:
        adj_list = self.generate_adj_list(V, E)
        in_degree = [0 for _ in range(V)]
        for u, v in E:
            in_degree[u] += 1

        q = deque()
        for v in range(V):
            if in_degree[v] == 0:
                q.append(v)

        topo_order = []
        visited_nodes = 0
        while q:
            node = q.popleft()
            topo_order.append(node)
            visited_nodes += 1
            for neighbour in adj_list[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.append(neighbour)
        
        if visited_nodes == V:
            print(topo_order)
            # return topo_order, has no cycle
            return topo_order
        else:
            # return "has atleast 1 cycle"
            return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Solution().canFinish(numCourses, prerequisites)