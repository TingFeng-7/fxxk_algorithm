from collections import deque
from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# 图的经典问题：
# 课程表，图的克隆
 
class Solution:
    #todo 课程表 2
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        res = []
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        print(indegrees)
        print(adjacency)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft() # 弹出第一个节点
            res.append(pre) #加入遍历结果当中
            numCourses -= 1 # 课程数减 1
            for cur in adjacency[pre]: # 该节点连接 的所有邻居入度 减 1
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur) # 如果入度恰好减到 0, 该节点加入队列
        return [] if  numCourses else res #返回 如果课程数没减完 返回空[]
    
    #todo 课程表 1
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        # Get the indegree and adjacency of every course.
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        print(indegrees)
        print(adjacency)
        # Get all the courses with the indegree of 0.
        for i in range(len(indegrees)):
            if not indegrees[i]: queue.append(i)
        # BFS TopSort.
        while queue:
            pre = queue.popleft() # 弹出第一个节点
            numCourses -= 1 # 课程数减 1
            for cur in adjacency[pre]: # 该节点连接 的所有邻居入度 减 1
                indegrees[cur] -= 1
                if not indegrees[cur]: queue.append(cur) # 如果入度恰好减到 0, 该节点加入队列
        return not numCourses #返回 课程数减完没
    
    #todo 113 
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import defaultdict
        hashmap = defaultdict()

        def dfs(node: 'Node'):
            if not node:
                return
            if node.val in hashmap: #todo 因为是val 唯一对应 这个节点，所以可以 key：val --> root.val: clone_node
                return hashmap[node.val]
            clone_node = Node(node.val, [])
            hashmap[node.val] = clone_node
            print(hashmap)
            for next_node in node.neighbors:
                clone_node.neighbors.append(dfs(next_node))
            return clone_node

        return dfs(node)
        

