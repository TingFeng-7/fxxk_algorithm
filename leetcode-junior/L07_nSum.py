from typing import List


class Solution:
    # @ 2，两数之和 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}
        for i in range(len(nums)):
            # 查表，看看是否有能和 nums[i] 凑出 target 的元素
            need = target - nums[i]
            if need in valToIndex:
                return [valToIndex[need], i]
            # 存入 val -> index 的映射
            valToIndex[nums[i]] = i
        return []
    
    # @ 16. 最接近的三数之和
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()         # 别忘了要先排序数组
        min_bias = float('inf')         # 记录三数之和 与 目标值的 最小偏差
        for i in range(len(nums) - 2):
            # 固定 nums[i] 为三数之和中的第一个数，
            # 然后对 nums[i+1..] 搜索接近 target - nums[i] 的两数之和
            sum_ = nums[i] + self.twoSumClosest(nums, i + 1, target - nums[i])
            min_bias = target - sum_ if abs(min_bias) > abs(target - sum_)  else min_bias
                
        return target - min_bias

    # 在 nums[start..] 搜索最接近 target 的两数之和
    def twoSumClosest(self, nums: List[int], start: int, target: int) -> int:
        lo, hi = start, len(nums) - 1
        # 记录两数之和与目标值的偏差
        min_bias = float('inf')
        while lo < hi:
            sum_ = nums[lo] + nums[hi]
            min_bias = target - sum_ if abs(min_bias) > abs(target - sum_)  else min_bias
            if sum_ < target:
                lo += 1
            else:
                hi -= 1
        return target - min_bias
    
    # 
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float('inf')
        for i in range(n - 2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue  # 优化三

            # 优化一
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                break

            # 优化二
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return s
                if s > target:
                    if s - target < min_diff:  # s 与 target 更近
                        min_diff = s - target
                        ans = s
                    k -= 1
                else:  # s < target
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    j += 1
        return ans
    # @ 三数之和 思想： target=0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:  break     #:1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue  #:2. skip the same nums[k]
            i, j = k + 1, len(nums) - 1
            
            while i < j:  #:3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res
    
    # @ 18. 四数之和
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for a in range(n - 3):  # 枚举第一个数
            x = nums[a]
            if a and x == nums[a - 1]:  # 跳过重复数字
                continue
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:  # 优化一
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for b in range(a + 1, n - 2):  # 枚举第二个数
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]:  # 跳过重复数字
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:  # 优化一
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                # 双指针枚举第三个数和第四个数
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]  # 四数之和
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:  # s == target
                        ans.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:  # 跳过重复数字
                            c += 1
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:  # 跳过重复数字
                            d -= 1
        return ans
