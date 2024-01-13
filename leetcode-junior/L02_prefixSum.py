from bisect import bisect_left
import random
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        sum = [0] * (n + 1)
        #? 数组前缀和 + hash
        for i in range(1, n+1):
            sum[i] = sum[i-1] + nums[i-1]

        s = {}
        for i in range(2, n+1):
            s[sum[i-2] % k] = s.get(sum[i-2] % k, 0) + 1  # 不需要value倒是
            if sum[i] % k in s:
                return True
        return False
    
    # @ 和为k的子数组
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefixSumCounts = defaultdict(int)
        prefixSumCounts[0] = 1

        for num in nums:
            prefixSum += num
            count += prefixSumCounts[prefixSum - k]
            prefixSumCounts[prefixSum] += 1

        return count

class Solution01:
    # 528  https://leetcode.cn/problems/random-pick-with-weight/description/
    def __init__(self, w: List[int]):
        n = len(w)
        self.prefix_sum = [0] * n
        self.prefix_sum[0] = w[0]
        
        # prefix_sum
        for i in range(1, n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + w[i]
        print(self.prefix_sum)

    def pickIndex(self) -> int:
        seed = random.randint(1, self.prefix_sum[-1])
        index = bisect_left(self.prefix_sum, seed)
        return index
