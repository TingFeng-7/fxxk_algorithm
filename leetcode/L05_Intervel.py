from typing import List


class Interval_Solution:
    # 435 https://leetcode.cn/problems/non-overlapping-intervals/
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        end = intervals[0][1]
        ans = 1
        for e in intervals[1:]:
            if e[0] > end:
                end = e[1]
                ans += 1
            # start = e[0]
        return n - ans

    # 452 https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        n = len(points)
        end = points[0][1]
        ans = 1
        for e in points[1:]:
            if e[0] > end:
                end = e[1]
                ans += 1
            # start = e[0]
        return ans
    
    # 763. 划分字母区间
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = [0] * 27 # hash数组记录每个字符最后出现的位置
        for i in range(len(S)):
            hashmap[ord(S[i]) - ord('a')] = i
        
        result = []
        left = 0
        right = 0
        for i in range(len(S)):
            right = max(right, hashmap[ord(S[i]) - ord('a')]) # 找到最远边界
            if i == right:
                result.append(right - left + 1)
                left = i + 1
                
        return result