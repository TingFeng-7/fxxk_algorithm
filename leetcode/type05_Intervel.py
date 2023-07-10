from typing import List


class Interval_Solution:
    # 435 https://leetcode.cn/problems/non-overlapping-intervals/
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x :x[1])
        n =len(intervals)
        end = intervals[0][1]
        ans=1
        for e in intervals[1:]:
            if e[0]>end:
                end=e[1]
                ans+=1
            # start = e[0]
        return n - ans
    #452 https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x :x[1])
        n =len(points)
        end = points[0][1]
        ans=1
        for e in points[1:]:
            if e[0]>end:
                end=e[1]
                ans+=1
            # start = e[0]
        return ans
