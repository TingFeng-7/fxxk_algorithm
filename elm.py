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

def merge(intervals):
    res = []
    intervals.sort(lambda x: x[0])
    res.append(intervals[0])
    for curr in intervals[:1]:
        last = res[-1]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res

def generate(n):
    size = n*2
    res = []
    def dfs(path,l_num,r_num):
        if l_num > n or r_num >n or r_num > l_num:
            return
        if len(path) == size and l_num == r_num:
            res.append(path[:])
            return
        dfs(path+'(', l_num+1, r_num)
        dfs(path+')', l_num, r_num+1)
    dfs("", 0,0)
    return res 

def permute(nums):
    res = []
    def backtrack(path, choice):
        if not choice:
            res.append(path[:])
            return
        for i in range(choice):
            backtrack(path+[choice[i]], choice[:i]+choice[i+1:])
    backtrack(nums, [])
    return res

def subsets(nums):
    res = []
    nums_len = len(nums)
    def backtrack(path, start):
        if len(path) > nums_len:
            return
        else:
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop(-1)
    backtrack(0, [])
    return res

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return list()
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    combination = []
    res = []
    def backtrack(index: int):
        if index == len(digits):
            res.append("".join(combination))
        else:
            digit = digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()
    backtrack(0)
    return res
class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.nxt = next
        
def reverse_iter(head):
    dummy = ListNode(-1)
    dummy.next = head
    prev, curr = None, head
    while curr:
        nxt_node = curr.nxt
        curr.nxt = prev
        prev , curr = curr, nxt_node
    return prev

def reverse_recursion(head):
    if head is None or head.nxt is None:
        return head
    last = reverse_recursion(head.nxt)
    head.nxt.nxt = head
    head.nxt = None
    return last
    
# def remove(head, n):
#     dhead = ListNode(-1, head)
#     slow, fast = dhead, dhead
#     while n > 0:
#         fast = fast.nxt
#         n-=1
#     while fast:
        
def isSameTree(p, q):
    if p ==None and q==None:
        return True
    if p is None or q is None:
        return False
    return p.val == q.val and \
        isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
        
        
if __name__ =='__main__':
    arr = [1,3,4,5,2,3]
    quicksort(arr, 0, len(arr)-1)
    print(arr) 
    topKSplit(arr, 0, len(arr)-1, 2)