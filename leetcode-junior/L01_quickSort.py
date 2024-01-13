from typing import List
import random

#@ 一些资料网址： https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/821137/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
# ! 快速排序＋快速选择

# ?1. 一直选取最左边为 pivot
def partition(arr: List[int], low: int, high: int) -> int:
    pivot, left, right = arr[low], low, high     # 双指针
    while left < right:
        while left < right and arr[right] >= pivot: right -= 1  
        arr[left] = arr[right]   #? 1. arr[right] 在右边，但却小于pivot
        while left < right and arr[left] <= pivot:  left += 1
        arr[right] = arr[left]   #? 2. arr[right] 在左边，但却大于pivot

    arr[left] = pivot       # pivot放置到中间left=right处
    
    return left

# ? 2. 随机选择pivot
def randomPartition(arr: List[int], low: int, high: int) -> int:
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
    return partition(arr, low, high)

# ? 215. 返回第K大元素
def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
    p = randomPartition(arr, low, high)
    if p == k - 1:                             # 第 K个 元素的下标为k-1
        return arr[p]  # !! 找到即返回
    elif p < k - 1:
        return topKSplit(arr, p+1, high, k)   # 递归对p右侧元素进行排序
    else:
        return topKSplit(arr, low, p-1, k)    # 递归对p左侧元素进行排序

# ? 5. Python 随机快排 
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]   # 将pivot放到数组最后,这样可以消除对位置的考虑
    
    left = [x for x in arr[:-1] if x < pivot]
    middle = [pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return randomized_quicksort(left) + middle + randomized_quicksort(right) #! Python特供写法

# @ 搜索旋转排序数组
def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:  #  if left < mid
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:   # 2 mid < right 
            if nums[mid] < target <= nums[len(nums) - 1]: 
                l = mid + 1
            else:
                r = mid - 1
    return -1 
    # 这种方法的关键在于通过比较 nums[l] 和 nums[mid] 的大小关系，判断哪一部分是有序的，
    # 从而确定目标值可能存在的区间，进而缩小搜索范围。这种思路使得算法的时间复杂度保持在 O(log n) 的水平。

# @ 第K大元素 就是递增数组（从1算起）的 n-(k-1)
# k 代表第几个 从 1 开始
def findKthLargest(nums: List[int], k: int) -> int:
    n = len(nums)
    # 第k大元素的坐标：代入n就理解了
    return topKSplit(nums, 0, n-1, n-k+1)
