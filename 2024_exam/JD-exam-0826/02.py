nums, games = list(map(int, input().split()))
nums_arr = [1] * nums
games_arr = [1] * games


for i in range(nums):
    nums_arr[i] = list(map(str, input().split()))
    # nums_arr.append(list(map(str, input().split())))
for i in range(games):
    games_arr[i] = list(map(str, input().split()))
    # games_arr.append(list(map(str, input().split())))

# print(nums_arr)
# print(games_arr)

res = ''
for game in games_arr:
    x, y, xi, yi = game
    dic = {}
    arrx, arry = nums_arr[int(x) - 1], nums_arr[int(y) - 1]
    if arrx[1] == -1 or arry[1] == -1:
        continue
        
    name_x, name_y = arrx[0], arry[0]
    if name_x == name_y:
        continue # 跳过

    else:
        dic[arrx[0]] = [arrx[1], xi]
        dic[arry[0]] = [arry[1], yi]
        # print(dic)
        if dic['human'][1] == 'N':
            if dic['monster'][1] == 'Y' and int(dic['human'][0]) > int(dic['monster'][0]):
                if nums_arr[int(x) - 1][0] == 'monster':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
            else:
                continue  # 人不暴露就没事

        elif dic['human'][1] == 'Y': # 人类明牌
            if int(dic['human'][0]) > int(dic['monster'][0]): # 战斗力胜出
                if nums_arr[int(x) - 1][0] == 'monster':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
            else: # 人没了
                if nums_arr[int(x) - 1][0] == 'human':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
        
for i in nums_arr:
    res += 'Y' if i[1] != -1 else 'N'
print(res)


nums, games = list(map(int, input().split()))
nums_arr = [1] * nums
games_arr = [1] * games
for i in range(nums):
    nums_arr[i] = list(map(str, input().split()))
    # nums_arr.append(list(map(str, input().split())))
for i in range(games):
    games_arr[i] = list(map(str, input().split()))
    # games_arr.append(list(map(str, input().split())))

# print(nums_arr)
# print(games_arr)

res = ''
for game in games_arr:
    x, y, xi, yi = game
    dic = {}
    arrx, arry = nums_arr[int(x) - 1], nums_arr[int(y) - 1]
    if arrx[1] == -1 or arry[1] == -1:
        continue
        
    name_x, name_y = arrx[0], arry[0]
    if name_x == name_y:
        continue # 跳过

    else:
        dic[arrx[0]] = [arrx[1], xi]
        dic[arry[0]] = [arry[1], yi]
        # print(dic)
        if dic['human'][1] == 'N':
            if dic['monster'][1] == 'Y' and int(dic['human'][0]) > int(dic['monster'][0]):
                if nums_arr[int(x) - 1][0] == 'monster':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
            else:
                continue  # 人不暴露就没事

        elif dic['human'][1] == 'Y': # 人类明牌
            if int(dic['human'][0]) > int(dic['monster'][0]): # 战斗力胜出
                if nums_arr[int(x) - 1][0] == 'monster':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
            else: # 人没了
                if nums_arr[int(x) - 1][0] == 'human':
                    nums_arr[int(x) - 1][1] = -1
                else:
                    nums_arr[int(y) - 1][1] = -1
        
for i in nums_arr:
    res += 'Y' if i[1] != -1 else 'N'
print(res)


