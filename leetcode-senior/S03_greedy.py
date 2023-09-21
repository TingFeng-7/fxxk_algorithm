from typing import List


class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i
    
    #@376 摆动序列
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: 
            return n
        
        prevdiff = nums[1] - nums[0]
        ret = 2 if prevdiff != 0 else 1
        
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
                
        return ret