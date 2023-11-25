def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1
    
    while num <= n * n:
        # 从左到右
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # 从上到下
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # 从右到左
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # 从下到上
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix


# @ 54. 螺旋矩阵
def spiralOrder(matrix):
    result = []
    m, n = len(matrix), len(matrix[0])
    left, right, top, bottom = 0, n - 1, 0, m - 1

    while left <= right and top <= bottom:
        # 从左到右
        for i in range(left, right + 1):
            result.append(matrix[top][i])

        # 从上到下
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        # 从右到左
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][i])

        # 从下到上
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])

        left += 1
        top += 1
        right -= 1
        bottom -= 1

    return result

# 示例
n = 3
result = generateMatrix(n)
for row in result:
    print(row)
    
# 示例
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = spiralOrder(matrix)
print(result)
