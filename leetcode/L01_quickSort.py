from typing import List
import random


def partition(arr: List[int], low: int, high: int) -> int:
    # ?1.一直选取最左边为 pivot
    pivot, left, right = arr[low], low, high     # 双指针
    while left < right:
        while left < right and arr[right] >= pivot:         
            right -= 1  
        arr[left] = arr[right]   # pivot的位置被占据
        while left < right and arr[left] <= pivot:          
            left += 1
        arr[right] = arr[left]    # left 前进，然后调到 right的位置

        # arr[left], arr[right] = arr[right], arr[left]
    arr[left] = pivot           # pivot放置到中间left=right处
    return left


def randomPartition(arr: List[int], low: int, high: int) -> int:
    # ?2.随机选择pivot
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # pivot放置到最左边
    return partition(arr, low, high)

# @ 随机快速排序
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    # 随机选择一个pivot
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    # 将pivot放到数组最后,这样可以消除对位置的考虑
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
    
    left = [x for x in arr[:-1] if x < pivot]
    middle = [pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

class Solution:
    # @ 搜索旋转排序数组
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:  # 1 left ... mid 升序
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # 2 right ... mid 升序
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    # @-n 第K大元素
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
            # p = partition(arr, low, high)  ，以p为分割点【非随机选择pivot】

            p = randomPartition(arr, low, high)
            if p == k - 1:                                      # 第k小元素的下标为k-1
                return arr[p]  # 【找到即返回】
            elif p < k - 1:
                return topKSplit(arr, p+1, high, k)           # 递归对p右侧元素进行排序
            else:
                return topKSplit(arr, low, p-1, k)            # 递归对p左侧元素进行排序

        n = len(nums)
        # 第k大元素的坐标：代入n就理解了
        return topKSplit(nums, 0, n-1, n-k+1)
