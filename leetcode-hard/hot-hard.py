class Solution:
    # @ 42 接雨水
    def trap(self, height: List[int]) -> int:
        #左右两边分别 单调栈，记录左右两边的最大高度
        n= len(height)
        left, right=[0]*n, [0]*n #两端存不住水
        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1]) #: 从左向右取最高
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i+1]) #: 从右向左取最高
        
        water = 0
        for i in range(n):
            water+= max(0, min(left[i],right[i])-height[i])
        return water