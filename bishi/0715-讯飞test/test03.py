n = int(input())
record = []
for i in range(n):
    string = input()
    k = input()
    record.append([string, k])
res = []
print(record)
for i, (s, k) in enumerate(record):
    count, ll = 1, 0
    sign_pos = []
    for si, ss in enumerate(s):
        flag, base = 0, 10
        if ss == '?':
            if si == 0:
                base = 9
                flag = 1
            count = count * base + base
            ll += 1
            sign_pos.append(si)
        else:
            continue
    if flag == 1:
        k[0]
    k_p, q_p = len(k)-1, len(sign_pos)-1
    new_s = list(s)
    while k_p > 0 and q_p > 0:
        last = k[k_p]
        s[q_p] = last
        k_p -= 1
        q_p -= 1


for ans in res:
    print("".join(ans))


# print(n,list1)
n = len(string)
i, j = 0, 0
L = 0
res = []
while j < n:
    base = string[i]
    while j < n and string[j] == base:  # 只要当前字符等于它
        # print(i, j)
        j += 1
    L = j-i  # 记录下长度
    if L < 3:
        print(-1)
    elif L >= 3:  # 分情况
        if L % 2 == 1:  # 奇数
            res.append(base*L)
        elif L >= 8:  # 偶数 必须大于8
            res.append(base * 3)
            res.append(base*(L-3))
        else:
            print(-1)

    i = j

print(" ".join(res))
