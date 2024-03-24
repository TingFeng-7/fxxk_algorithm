from typing import List

class Solution:
    # Hard 84. 柱状图中最大的矩形
    def largestRectangleArea(self, heights: List[int]) -> int:
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
    
    # 739. 每日温度 （从后往前 维护一个 单调递增栈（top ==> down）
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #1. o(n2) 二重循环  #2. 单调栈
        s1, n =[], len(temperatures)
        res = [0 for _ in range(n)]
        if n==1: return [0]

        for i in range(n-1, -1 , -1):
            tmp = temperatures[i]
            while s1 and tmp >= s1[-1][1] : # 此时栈顶到栈底 是递增序列
                s1.pop() # 小于 当前温度 的 全部pop s1要有元素
            if len(s1)==0:
                res[i] = 0
            else:
                res[i] = s1[-1][0] - i
            s1.append([i, temperatures[i]])

        return res
    
    # 496.下一个更大元素 （从后往前 维护一个 单调递增栈（top ==> down）
    def nextGreaterElement(nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        s = []  
        # 倒着往栈里放
        # ======================Same===================================
        for i in range(n - 1, -1, -1):
            # 判定个子高矮
            while s and s[-1] <= nums[i]:
                s.pop() # 矮个起开，反正也被挡着了。。。
            res[i] = s[-1] if s else -1
            s.append(nums[i]) #@ 3. 元素入栈
        # ======================Same===================================
        return res
    
    # 503.下一个更大元素ll （从后往前 维护一个 单调递增栈（top ==> down）
    def nextGreaterElements_ii(self, nums: List[int]) -> List[int]:
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
        # 402 . 移除k位数字
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'
    
    def simplifyPath(self, path: str) -> str:
        # 71. 简化路径 跳过.符号，如果有.. 存在的话把栈跳出
        parts = path.split("/")
        stack = []
        # 借助栈计算最终的文件夹路径
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(part)
        # 栈中存储的文件夹组成路径
        res = ""
        while stack:
            res = '/' + stack.pop() + res
        return res if res else '/'
    
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