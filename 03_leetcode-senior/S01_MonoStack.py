# 84. 柱状图中最大的矩形
# 739. 每日温度
# 496.下一个更大元素 
# 503.下一个更大元素ll 
# 42. 接雨水
# 402. 移除k位数字
# 316. 去除重复字母
from typing import List
import collections

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Hard 84. 柱状图中最大的矩形
        # 如果heights为空，则返回0
        if not heights:
            return 0

        n = len(heights)
        left_i = [0] * n
        right_i = [0] * n

        left_i[0] = -1
        right_i[-1] = n
        #递增传递性
        for i in range(1, n):
            # 将i-1的索引设置为tmp
            tmp = i - 1
            # 当tmp不等于-1且heights[tmp]大于heights[i]时，tmp索引设置为left_i[tmp]
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            # 将tmp索引设置为i
            left_i[i] = tmp

        for i in range(n - 2, -1, -1):
            # 将i+1的索引设置为tmp
            tmp = i + 1
            # 当tmp不等于n且heights[tmp]大于heights[i]时，tmp索引设置为right_i[tmp]
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            # 将tmp索引设置为i
            right_i[i] = tmp

        res = 0
        # 遍历heights
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res
    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 739 每日温度
        n = len(temperatures)
        ans = [0] * n
        st = [] # 栈 记录温度索引
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

    def nextGreaterElement(nums: List[int]) -> List[int]:
        # 496.下一个更大元素 
        n = len(nums)
        res = [0 for _ in range(n)]
        s = []  
        # ======================Same===================================
        for i in range(n - 1, -1, -1):
            # 判定个子高矮
            while s and nums[i] >=s [-1]:
                s.pop() 
            res[i] = s[-1] if s else -1
            s.append(nums[i]) 
        # ======================Same===================================
        return res
    

    def nextGreaterElements_ii(self, nums: List[int]) -> List[int]:
        # 503.下一个更大元素ll 
        n = len(nums)
        res = [-1 for _ in range(n)]
        stack = []
        # ======================Same===================================
        for i in range(n * 2):
            while stack and  nums[stack[-1]] <= nums[i % n]:
                u = stack.pop()
                res[u] = nums[i % n]

            stack.append(i % n) #@ 3. index入栈
        # =========================================================
        return res

    def trap(self, height: List[int]) -> int:
        # 42. 接雨水
        #左右两边分别 单调栈，记录左右两边的最大高度
        n= len(height)
        left, right=[0]*n, [0]*n #两端存不住水
        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i+1])
        
        water = 0
        for i in range(n):
            water+= max(0, min(left[i],right[i])-height[i])
        return water
    
    # ? https://leetcode.cn/problems/remove-duplicate-letters/solutions/290200/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
    def removeKdigits(self, num, k):
        # 402. 移除k位数字
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and digit < stack[-1] : 
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'
    
    
    def removeDuplicateLetters(self, s) -> int:
        # 316. 去除重复字母
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)