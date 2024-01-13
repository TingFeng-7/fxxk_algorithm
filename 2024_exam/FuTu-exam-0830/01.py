N = int(input())
mat = [[0] * N for _ in range(N)]
for i in range(N):
    mat[i] = list(map(int, input().split()))

from math import gcd

res = []

# for row in mat:
#     row.sort()
#     a,b,c,d = row
#     # 求出 四个数的 最小公约数
#     print(a,b,c,d)
#     g = gcd(a,gcd(b,gcd(c,d)))
#     res.append(g if g!=1 else -1)

for i in range(N):
    print(res[i])