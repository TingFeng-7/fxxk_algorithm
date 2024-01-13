from typing import List
# 方向数组，分别代表上、下、左、右
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(grid: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> None:
    m, n = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n:  # ? 超出索引边界
        return
    if visited[i][j]:  # 已遍历过 (i, j)
        return
    visited[i][j] = True  # 进入节点 (i, j)

    for d in dirs:   # 递归遍历上下左右的节点
        next_i = i + d[0]
        next_j = j + d[1]
        dfs(grid, next_i, next_j, visited)



def floodfill(grid: List[List[str]], i: int, j: int) -> None:
    m, n = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' :  # ? 超出索引边界 或 代码表示是海水的话，就直接返回
        return
    grid[i][j] = '0'  # todo  将原本的陆地 (i, j) 变成海水
    dfs(grid, i + 1, j)   # 淹没上下左右的陆地
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)


class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' :  # ? 超出索引边界 或 代码表示是海水的话，就直接返回
            return
        grid[i][j] = '0'  # todo  将原本的陆地 (i, j) 变成海水
        # 淹没上下左右的陆地
        dfs(grid, i + 1, j)  
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)
    
    # 思想就是 二维遍历 + 漫水算法
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])  # ? 遍历 grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1 # 每发现一个岛屿，岛屿数量加一
                    self.dfs(grid, i, j) # 然后使用 DFS 将岛屿淹了
        return res

    # 79. 单词搜索
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False