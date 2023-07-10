# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码还未经过力扣测试，仅供参考，如有疑惑，可以参照我写的 java 代码对比查看。
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
    # 进入节点 (i, j)
    visited[i][j] = True
    # 递归遍历上下左右的节点
    for d in dirs:
        next_i = i + d[0]
        next_j = j + d[1]
        dfs(grid, next_i, next_j, visited)
    # 离开节点 (i, j)

# 从 (i, j) 开始，将与之相邻的陆地都变成海水
def floodfill(self, grid: List[List[str]], i: int, j: int) -> None:
    m, n = len(grid), len(grid[0])
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