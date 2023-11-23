from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            need_val = target-nums[i]
            if need_val in record:
                return [record[need_val], i]
            else:
                record[nums[i]] = i
        return [0, 0]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # ? 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # ? 2. skip the same `nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:  # ? 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
