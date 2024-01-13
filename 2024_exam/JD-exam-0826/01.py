num = int(input())
query = list(map(int, input().split()))

res = [0] * num
dic = {}
# res 不能相等
idx = 0
for val in query:
    idx+=1
    temp = idx - (val % idx)
    if temp == 0:
        temp += idx
    while temp in dic:
        temp += idx
    dic[temp] = 1
    res[idx-1] = temp

print(' '.join(map(str, res)))