nums = [1, 6, 7, 8]
moveFrom = [1, 7, 2]
moveTo = [2, 9, 5]
nums = list(set(nums))
n = len(nums)
hashmap = {}
for i in range(n):
    hashmap[nums[i]] = i
print(hashmap)
for i in range(len(moveFrom)):
    det = moveFrom[i]
    add = moveTo[i]
    if det == add:
        continue
    # 找索引
    idx = hashmap[det]
    nums[idx] = add
    hashmap[add] = idx
print(nums.sort())
