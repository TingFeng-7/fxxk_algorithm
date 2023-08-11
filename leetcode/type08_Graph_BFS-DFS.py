from typing import List
# 方向数组，分别代表上、下、左、右
dirs = [[-1,0], [1,0], [0,-1], [0,1]]

def dfs(grid: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> None:
    m, n = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n:
        # 超出索引边界
        return
    if visited[i][j]:
        # 已遍历过 (i, j)
        return
    visited[i][j] = True     # 进入节点 (i, j)
    
    for d in dirs:     # 递归遍历上下左右的节点
        next_i = i + d[0]
        next_j = j + d[1]
        dfs(grid, next_i, next_j, visited)
    # 离开节点 (i, j)

#todo 从 (i, j) 开始，将与之相邻的陆地都变成海水
def floodfill(self, grid: List[List[str]], i: int, j: int) -> None:
    m, n = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n:
        # 超出索引边界
        return
    if grid[i][j] == '0': # 0 代表是海水，就直接返回1
        return

    grid[i][j] = '0'  #todo  将原本的陆地 (i, j) 变成海水

    self.dfs(grid, i + 1, j)   # 淹没上下左右的陆地
    self.dfs(grid, i, j + 1)
    self.dfs(grid, i - 1, j)
    self.dfs(grid, i, j - 1)