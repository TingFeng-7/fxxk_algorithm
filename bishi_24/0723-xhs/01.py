m, n, k = map(int, input().split(' '))
base = k - 1
remain = m - k #剩下的长度，
# 每一个区间要占两个数
group = remain // 2
if group < n-1:  #还要 n-1 个区间
    print(base)
elif remain - 2*group  > base:
    print(remain - 2*group)
else:
    print(base)