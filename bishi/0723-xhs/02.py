qs = int(input())


def SonMaxSum(arr):
    l = len(arr)
    if l == 1:
        return arr[0]
    dp = [0] * l
    dp[0] = arr[0]
    for i in range(1, l):
        dp[i] = max(dp[i-1]+arr[i], arr[i])
    return max(dp)


maxVal = -1 * float('inf')
res = [0] * qs
for i in range(qs):
    m, val = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    arr_min = min(arr)
    arr_max = max(arr)
    if val < arr_min:
        res[i] = SonMaxSum(arr)
        continue
    if arr_min > 0:  # val >= arr_min
        res[i] = sum(arr) + val - arr_min
        continue
    if arr_max <= 0 and val >= 0:
        res[i] = arr_max + val

    for j in range(len(arr)):
        if val <= arr[j]:
            continue
        maxVal = max(maxVal, SonMaxSum(arr[:j]+[val]+arr[j+1:]))
    res[i] = maxVal
    maxVal = -1 * float('inf')

for i in res:
    print(i)
