n = int(input())
string = input()
# print(n,list1)
n = len(string)
i,j = 0,0
L=0
res = []
while j < n:
    base = string[i]
    while j < n and string[j] == base: # 只要当前字符等于它
        # print(i, j)
        j+=1
    L = j-i #记录下长度
    if L < 3:
        print(-1)
    elif L >= 3: #分情况
        if L % 2 == 1: #奇数
            res.append(base*L)
        elif L >= 8: #偶数 必须大于8
            res.append(base * 3)
            res.append(base*(L-3))
        else:
            print(-1)

    i = j

print(" ".join(res))