# 小明小红战斗力
# inputs = list(map(int, input().split(" ")))
# nums, operations = inputs[0], inputs[1]
# # print(str(nums), str(operations))
# power = list(map(int, input().split(" ")))
# while operations!=0:
#     inputs = list(map(int, input().split(" ")))
#     name, k = inputs[0], inputs[1]
#     # print(power[:k])
#     tmp = power[:k]
#     if name==1:
#         tmp.sort()
#         power[:k] = tmp
#         # print(f'name:{name}:从小到大 {power}')
#     elif name==2:
#         tmp.sort(reverse=True) #act #cheack
#         power[:k] = tmp
#         # print(f'name:{name}:从大到小 {power}')
#     operations-=1

# s=""
# for i in range(nums):
#     s+=str(power[i])
#     if i != nums-1:
#         s+=" "
# print(s)

# print('end')
# print(f'power: {power}')

# todo 3.多个测试案例，每个测试案例多行
# while 1:
#     nm = list(map(int,input().split(" ")))
#     N = nm[0]
#     M = nm[1]
#     print(str(N)+' '+str(M))
#     for i in range(M):
#         abc = list(map(int, input().split(" ")))
#         a, b, c = abc[0], abc[1], abc[2]
#         print(str(a)+'_'+str(b)+'_'+str(c))

# inputs = list(map(int, input().split(" ")))
# L, R = inputs[0], inputs[1]
# digits=0
# if R<10:
#     print(str(R))
# else:
#     tmp = R
#     while tmp:
#         tmp = tmp//10
#         digits+=1
#     digits-=1
#     print(f'{(pow(10,digits)-1)}* 9 *{digits}')
#     print(str((pow(10,digits)-1)*9*(digits-1)))
# @ 腾讯
# inputs = input()
# res=[]
# def bactrack(path, choices, depth):
#     if depth==4: return
#     for char in choices:
#         path = path+char # do b
#         res.append(path)
#         bactrack(path, choices, depth+1)
#         path = path[:-1] #undo
# choices='abcdefghijklmnopqrstuvwxyz'
# bactrack("",choices,0)
# ll={}
# for k,v in enumerate(res):
#     ll[v] = k
# print(ll[inputs])

# @ 腾讯01 素数对

inputs = input()
count = 0

def isvalid(l):
    mid = l//2
    for i in range(2, mid):
        if l % i == 0:  # 除得尽
            return False
    return True

l = 2
r = int(inputs)-l
res = []
while (l <= r):
    if isvalid(l) and isvalid(r):
        count += 1
        res.append([l, r])
    l, r = l+1, r-1
print(res)
print(count)
