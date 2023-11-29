# https://leetcode.cn/problems/binary-tree-right-side-view/solutions/2015061/ru-he-ling-huo-yun-yong-di-gui-lai-kan-s-r1nc/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# :1. 快速排序 + partition
def partition(arr, low, high):
    pivot = arr[low]
    l,r = low, high
    while l < r:
        while l < r and arr[r] >= pivot:
            r -= 1
        arr[l] = arr[r]
        while l < r and arr[l] <= pivot:
            l += 1
        arr[r] = arr[l]
    arr[l] = pivot
    return l
    
# 1. 快速排序 + partition
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

arr = [1,3,2,2,0]
quicksort(arr, 0, len(arr)-1)
print(arr) 
    
# 2. 快速排序 + 额外数组
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)

#: 2. bfs模版题
from collections import deque
def bfs(graph, start):
    # 创建队列并加入起始节点
    queue = deque([start])
    
    # 记录已访问的节点，防止重复访问
    visited = set([start])
    
    while queue:
        # 出队列
        node = queue.popleft()
        
        # 处理当前节点
        # TODO: 根据问题的要求进行处理
        # 将当前节点的未访问邻居加入队列
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# 示例：二叉树的层次遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @102 层序遍历
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    return result

#@ 200 岛屿数量
def numIslands(self, grid: List[List[str]]) -> int:
    
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None: # 从 (i, j) 开始，将与之相邻的陆地都变成海水
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            # 超出索引边界
            return
        if grid[i][j] == '0':
            # 已经是海水了
            return
        # 将 (i, j) 变成海水
        grid[i][j] = '0'
        # 淹没上下左右的陆地
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
    
    res = 0
    m = len(grid)
    n = len(grid[0])
    # 遍历 grid
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                # 每发现一个岛屿，岛屿数量加一
                res += 1
                # 然后使用 DFS 将岛屿淹了
                self.dfs(grid, i, j)
    return res

# @ 130. 被围绕的区域 
def solve(self, board: List[List[str]]) -> None:
    if not board:
        return
    
    n, m = len(board), len(board[0])

    def dfs(x, y):
        if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
            return
        
        board[x][y] = "A"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    for i in range(n):
        dfs(i, 0)
        dfs(i, m - 1)
    
    for i in range(m - 1):
        dfs(0, i)
        dfs(n - 1, i)
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "A":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"
    
# @ 199 二叉树的右视图
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level[-1])
            # else:
                # result.append(current_level[-1])
            # level += 1
        return result
    
# @ 117. 填充指针 BFS 层序遍历
def connect(self, root: 'Node') -> 'Node':
    if root is None:
        return None
    queue = deque([root])
    while queue:
        n = len(queue)
        last = None
        for _ in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if last:
                last.next = node
            last = node
    return root
