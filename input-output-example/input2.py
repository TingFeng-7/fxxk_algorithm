
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
