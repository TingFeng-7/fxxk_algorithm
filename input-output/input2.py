
# -n 1.测试组数不固定，每组三行数据
# input = int(input())
# output = input
# print(str(output))

# -n 2.单行多个输入，单行多个输出，空格分割 (多行输入，每一行是一个测试样例)
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

# -n 3.多个测试案例，每个测试案例多行
# while 1:
#     nm = list(map(int,input().split(" ")))
#     N = nm[0]
#     M = nm[1]
#     print(str(N)+' '+str(M))
#     for i in range(M):
#         abc = list(map(int, input().split(" ")))
#         a, b, c = abc[0], abc[1], abc[2]
#         print(str(a)+'_'+str(b)+'_'+str(c))

inputs = input().split(" ")  # ! 字符串
inp = list(map(int, inputs))  # ! 将每个str转为int，形成链表

print(inputs, inp)  # 输入转为列表
L, R = inputs[0], inputs[1]
print(L + R)
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
