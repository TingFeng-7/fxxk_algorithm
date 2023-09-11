from typing import List


class Solution:
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
