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
    # 33
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n+1
        while l + 1 < r:
            m = (l+r)//2
            if m*(m+1)/2 <= n:
                l = m
            else:
                r = m
        return l

    # 04
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2.0
    
    # 寻找第k小
    def findKth(self, nums1, i, nums2, j, k):
        if i >= len(nums1): # i,j 分别是两个数组的 start
            return nums2[j + k - 1]  # nums1 is an empty array
        if j >= len(nums2):
            return nums1[i + k - 1]  # nums2 is an empty array
        if k == 1:
            return min(nums1[i], nums2[j])
        half_k = k//2
        midVal1 = nums1[i + half_k - 1] if i + half_k - 1 < len(nums1) else float('inf')
        midVal2 = nums2[j + half_k - 1] if j + half_k - 1 < len(nums2) else float('inf')
        if midVal1 < midVal2: # 比较两个 大哥谁更小
            # 已经派出了 half_k个元素
            return self.findKth(nums1, i + half_k, nums2, j, k - half_k)
        else:
            return self.findKth(nums1, i, nums2, j + half_k, k - half_k)