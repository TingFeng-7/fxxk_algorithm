from typing import List

# 二分的本质
# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/solutions/705486/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/
class Solution:
    # https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/134812/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/
    # 一文解决四道搜索旋转排序数组
    
    #@153. 寻找旋转排序数组中的最小值
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]: # 说明 该区间 连续递增
                r = mid
            elif nums[mid] > nums[r]:
            # else:
                l = mid + 1
        return nums[l]
    
    def findMin(self, nums: List[int]) -> int:
        left, right =0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            mid = left + (right-left)//2
            if nums[left] <= nums[mid]:
                left = mid +1
            else:
                right = mid
        return -1
    
    # @ 下一个最大字符
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        if ord(letters[-1]) - ord(target) < 1:
            return letters[0]
        while l < r:
            mid = l+(r-l)//2
            print(letters[mid])
            if ord(letters[mid]) - ord(target) < 1:
                l = mid+1
            elif ord(letters[mid]) - ord(target) >= 1:  # 收缩区间
                r = mid
        return letters[r]
    
    # @ 33 搜索旋转排序数组
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
    
    # @ 34. 在排序数组中查找元素的第一个和最后一个位置
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
    
    # ? 二分找元素的左边界
    def left_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 搜索区间为 [left, right]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:  # 1 搜索区间变为 [mid+1, right]
                left = mid + 1
            elif nums[mid] >= target: # 2 搜索区间变为 [left, mid-1] and 收缩右侧边界
                right = mid - 1
            elif nums[mid] == target: # 2 搜索区间变为 [left, mid-1] and 收缩右侧边界
                right = mid - 1
        # 检查出界情况
        if left >= len(nums) or nums[left] != target: 
            return -1
        return left
    
    # ? 二分找 元素右边界
    def right_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target: # 这里改成收缩左侧边界即可
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        # 这里检查 right 越界
        if right < 0 or nums[right] != target: 
            return -1
        return right
    
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n+1
        while l + 1 < r:
            m = (l+r) // 2
            if m*(m+1)/2 <= n:
                l = m
            else:
                r = m
        return l


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(self, nums1, i, nums2, j, k):
            if i >= len(nums1): 
                return nums2[j + k - 1] 
            if j >= len(nums2):
                return nums1[i + k - 1] 
            if k == 1:
                return min(nums1[i], nums2[j])
            half_k = k // 2
            midVal1 = nums1[i + half_k - 1] if i + half_k - 1 < len(nums1) else float('inf')
            midVal2 = nums2[j + half_k - 1] if j + half_k - 1 < len(nums2) else float('inf')
            
            if midVal1 < midVal2:  
                return self.findKth(nums1, i + half_k, nums2, j, k - half_k)
            else:
                return self.findKth(nums1, i, nums2, j + half_k, k - half_k)
            
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right)) / 2.0
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        寻找两个正序数组的中间值

        Args:
            nums1 (List[int]): _description_
            nums2 (List[int]): _description_

        Returns:
            float: _description_
        """        
        def k_min(start1,end1,start2,end2,k):
            cur_nums1 = end1-start1+1
            cur_nums2 = end2-start2+1
            if cur_nums1 == 0:
                return nums2[start2+k-1]
            if cur_nums2 == 0:
                return nums1[start1+k-1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            m1 = start1 + min(cur_nums1, k//2) - 1
            m2 = start2 + min(cur_nums2, k//2) - 1
            if nums1[m1] <= nums2[m2]:
                return k_min(m1+1,end1,start2,end2,k-(m1-start1+1))
            else:
                return k_min(start1,end1,m2+1,end2,k-(m2-start2+1))
            
        m,n = len(nums1),len(nums2)
        a,b = (m+n+1)//2, (m+n+2)//2
        x = k_min(0,m-1,0,n-1,a)
        y = k_min(0,m-1,0,n-1,b)
        return (x+y)/2

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        74. 搜索二维矩阵
        Args:
            matrix (List[List[int]]): 二维数组
            target (int): 寻找目标

        Returns:
            bool: _description_
        """        
        m, n = len(matrix), len(matrix[0])
        x,y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False   
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        240. 搜索二维矩阵 II
        Args:
            matrix (List[List[int]]): _description_
            target (int): _description_

        Returns:
            bool: _description_
        """        
        r = len(matrix) # 行
        c = len(matrix[0]) # 列
        # 排除只有单行 单列 的情况
        if r == 1:
            return target in matrix[0]
        if c == 1:
            return target in [i for j in matrix for i in j]
        i, j = 0, c-1   # 以右上角元素为起点
        while j >= 0 and i < r:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1 # 左移
            if matrix[i][j] < target:
                i += 1 # 下移 
        return False
