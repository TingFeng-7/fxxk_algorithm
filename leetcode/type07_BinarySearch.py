from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r = 0 , len(letters)
        if ord(letters[-1]) - ord(target) < 1:
            return letters[0]
        while l<r:
            mid = l+(r-l)//2
            print(letters[mid])
            if ord(letters[mid])- ord(target) < 1:
                l = mid+1
            elif ord(letters[mid])- ord(target) >= 1: #收缩区间
                r = mid
        return letters[r]
    
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n+1
        while l + 1 < r:
            m = (l+r)//2
            if m*(m+1)/2 <= n:
                l = m
            else:
                r = m
        return l
    #-n 34
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
    
    def left_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 搜索区间为 [left, right]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:  # 1 搜索区间变为 [mid+1, right]
                left = mid + 1
            elif nums[mid] > target: # 2 搜索区间变为 [left, mid-1]
                right = mid - 1
            elif nums[mid] == target:  # 3 收缩右侧边界
                right = mid - 1
        # 检查出界情况
        if left >= len(nums) or nums[left] != target: 
            return -1
        return left
    
    def right_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target: # 这里改成收缩左侧边界即可
                left = mid + 1
        # 这里检查 right 越界
        if right < 0 or nums[right] != target: 
            return -1
        return right