import random
from typing import List
def partition(arr,left,right):
    pivot = arr[left]
    l, r = left, right
    while l < r:
        if l < r and arr[r] >= pivot:
            r -= 1
        arr[l] = arr[r]
        if l < r and arr[l] <= pivot:
            l += 1
        arr[r] = arr[l]
    arr[l] = pivot
    return l

def random_partition(arr, left, right):
    i = random.randint(left, right)
    arr[left], arr[i] = arr[i], arr[left]
    return partition(arr, left, right)

def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)


    
def search(nums, target):
    if not nums:
        return -1
    l,r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]: 
                l = mid + 1
            else:
                r = mid - 1
    return -1 

def topKSplit(arr, low, high, k):
    p = random_partition(arr, low, high)
    if p == k-1:
        print(arr[p])
        return arr[p]
    elif p < k-1:
        return topKSplit(arr, p+1, high, k)
    else:
        return random_partition(arr, low, p-1, k)
    
def findKthLargest(nums, k):
    n = len(nums)
    return topKSplit(nums, 0, n-1, n-k+1)

def twoSum(nums, taget):
    valToindex = {}
    for i in range(len(nums)):
        need = taget - nums[i]
        if need in valToindex:
            return [valToindex[i], i]
        else:
            valToindex[nums[i]] = i
    return[i]

def twoSumClosest(nums: List[int], start: int, target: int) -> int:
    lo, hi = start, len(nums) - 1
    # 记录两数之和与目标值的偏差
    min_bias = float('inf')
    while lo < hi:
        sum_ = nums[lo] + nums[hi]
        
        if abs(min_bias) > abs(target - sum_):
            min_bias = target - sum_  
        else:
            min_bias
            
        if sum_ < target:
            lo += 1
        else:
            hi -= 1
    return target - min_bias
    
def threeSumClosest(nums, target):
    if len(nums) < 3:
        return 0
    nums.sort()
    min_bias = float('inf')
    for i in range(len(nums)-2):
        sum_ = nums[i] + twoSumClosest(nums, i+1, target-nums[i])
        if abs(min_bias) > abs(target-sum_):
            min_bias = target - sum_
    return target - min_bias
    
def subarraysum(nums, k):
    prefixsum = 0
    count = 0
    prefixsumCount = {}
    prefixsum[0]=1
    
    for num in nums:
        prefixsum += num
        if prefixsum - k in prefixsumCount:
            count += prefixsumCount[prefixsum - k]
        prefixsumCount[prefixsum] += 1
    
    return count

def lengthOfLongestSubstring(s: str):
    window = {}
    left, right = 0, 0
    res = 0
    while right < len(s):
        add_c = s[right]
        right += 1
        window[add_c] = window.get(add_c, 0) + 1
        
        while window[add_c]>1:
            del_c = s[left]
            window[del_c] -= 1
            left += 1
        res = max(res, right - left)
    return res

if __name__ =='__main__':
    arr = [1,3,4,5,2,3]
    quicksort(arr, 0, len(arr)-1)
    print(arr) 
    topKSplit(arr, 0, len(arr)-1, 2)