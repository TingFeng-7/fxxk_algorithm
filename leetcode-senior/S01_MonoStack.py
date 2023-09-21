from typing import List


class Solution:
    #@ Hard 84. 柱状图中最大的矩形
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 如果heights为空，则返回0
        if not heights:
            return 0
        # 获取heights的长度
        n = len(heights)
        # 初始化left_i和right_i
        left_i = [0] * n
        right_i = [0] * n
        # 将left_i的第一个元素设置为-1
        left_i[0] = -1
        # 将right_i的最后一个元素设置为n
        right_i[-1] = n
        # 遍历heights
        for i in range(1, n):
            # 将i-1的索引设置为tmp
            tmp = i - 1
            # 当tmp不等于-1且heights[tmp]大于heights[i]时，tmp索引设置为left_i[tmp]
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            # 将tmp索引设置为i
            left_i[i] = tmp
        # 遍历heights
        for i in range(n - 2, -1, -1):
            # 将i+1的索引设置为tmp
            tmp = i + 1
            # 当tmp不等于n且heights[tmp]大于heights[i]时，tmp索引设置为right_i[tmp]
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            # 将tmp索引设置为i
            right_i[i] = tmp
        # 初始化res
        res = 0
        # 遍历heights
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res
    
    #@ 739. 每日温度 （从后往前 维护一个 单调递增栈（top ==> down）
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #1. o(n2) 二重循环
        #2. 单调栈
        s1, n =[], len(temperatures)
        s1.append([n-1, temperatures[-1]])
        res = [0] * n
        if n==1: return [0]
        # print(n,s1)
        for i in range(n-2, -1 , -1):
            tmp = temperatures[i]
            # print(i ,tmp, s1)
            while s1 and tmp >= s1[-1][1] : # 此时栈顶到栈底 是递增序列
                s1.pop() # 小于 当前温度 的 全部pop s1要有元素
            if len(s1)==0:
                res[i] = 0
            else:
                res[i] = s1[-1][0] - i
            s1.append([i, temperatures[i]])
        # print(res)
        return res
    #@ 496.下一个更大元素 （从后往前 维护一个 单调递增栈（top ==> down）
    def nextGreaterElement(nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(n)]
        s = []  #@ 1.先声明 栈和 ans 数组
        # 倒着往栈里放
        for i in range(n - 1, -1, -1):
            # 判定个子高矮
            while s and s[-1] <= nums[i]:
                # 矮个起开，反正也被挡着了。。。
                s.pop()
            res[i] = s[-1] if s else -1
            s.append(nums[i]) #@ 3. 小元素入栈
        return res
    
    #@ 503.下一个更大元素ll （从后往前 维护一个 单调递增栈（top ==> down）
    def nextGreaterElements_ii(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]:
                u = stack.pop()
                res[u] = nums[i % n]

            stack.append(i % n) #@ 3. 小元素入栈
            
        return res