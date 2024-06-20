from typing import List
#  55. 跳跃游戏

class Solution:
    # @ 55. 跳跃游戏
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n - 1):
            # 不断计算能跳到的最远距离
            farthest = max(farthest, i + nums[i])
            # 可能碰到了 0，卡住跳不动了
            if farthest <= i:
                return False
        return farthest >= n - 1

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


    # @ 376. 摆动序列
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n

        prevdiff = nums[1] - nums[0]
        ret = 2 if prevdiff != 0 else 1
        
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
                
        return ret