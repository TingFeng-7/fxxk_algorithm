s = input().strip()  # 1.去除左右空格
k = int(input())  # 2. 输入转 int
print(f'input : {s}')
print(f'input : {k}')
A = []
for i in range(len(s)-k):
    A.append(s[i:i+k])
if k == 1:
    A = sorted(A, key=lambda x: (x[0]))
elif k == 2:
    A = sorted(A, key=lambda x: (x[0], x[1]))
elif k == 3:
    A = sorted(A, key=lambda x: (x[0], x[1], x[2]))
elif k == 4:
    A = sorted(A, key=lambda x: (x[0], x[1], x[2], x[3]))
else:
    A = sorted(A, key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
print(A[0])
