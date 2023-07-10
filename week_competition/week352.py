# nums = [4,4,4]
# threshold = 8

# nums = [3,2,5,4]
# threshold = 5

# start, end = 0,0
# n = len(nums)
# maxl = 0
# while start < n :
#     # print(start)
#     while start < n and (nums[start] % 2!=0 or nums[start] > threshold) :
#         start+=1
#     end = start
#     path = 0
#     # print('srart',start)
#     while end < n:
#         if nums[end] %2 == 0 and nums[end]<=threshold:
#             # print('even')
#             path+=1
#         else:
#             break
#         if end+1 <n and nums[end+1] %2 == 1 and nums[end+1]<=threshold:
#             # print('odd')
#             path+=1
#         else:
#             break
#         end+=2
#     # print(start,end)
#     # print('path',path)
#     maxl = max(maxl, path)
#     start+=1
#     end =start
#     # print(end)

# print('res',maxl)

n=10
res= []
import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n+1, 2):
        if n % i == 0:
            return False
    return True

for i in range(2, n//2+1):
    if not is_prime(i) or not is_prime(n-i):
        continue

    res.append([i , n-i])
print(res)