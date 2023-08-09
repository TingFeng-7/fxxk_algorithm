n = int(input())
list1 = input().split(' ')
# print(n,list1)
string = "".join(list1)
n = len(string)
for e in string:
    if e == '0':
        n-=1
print(n)
