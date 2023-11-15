from math import log
N = int(input())
mat = [[0] * N for _ in range(N)]
for i in range(N):
    mat[i] = list(map(int, input().split()))

n = log(N, 2)
for r in range(n):
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            temp = [mat[i][j], mat[i][j + 1], \
                    mat[i + 1][j], mat[i + 1][j + 1]]
            mat[i][j] = temp.sort()[1]
print(mat[0][0])