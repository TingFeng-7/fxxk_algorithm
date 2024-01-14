from typing import List

# 区间问题的思想主要还是利用自定义sort
class Interval_Solution:
    # @ 56. 合并区间
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # 按区间的 start 升序排列
        intervals.sort(key=lambda a: a[0])
        res.append(intervals[0])
        for curr in intervals[1:]:
            # res 中最后一个元素的引用
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                # 处理下一个待合并区间
                res.append(curr)
        return res
    
    # @ 435 非重叠区间
    # https://leetcode.cn/problems/non-overlapping-intervals/
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # 按区间的 end 升序排序
        intervals.sort(key=lambda x: x[1]) 
        n = len(intervals)
        # 等价于求解该数组中 有多少非重叠区间
        end = intervals[0][1]
        ans = 1
        for e in intervals[1:]:
            if e[0] > end: # 当新元素的起始 > 上一元素的末尾时 才会更新 ，此时的ans代表数组不重叠qu'j
                end = e[1] # 结尾更新
                ans += 1
        return n - ans

    # @ 452 用最少数量的箭引爆气球 （完全不重叠的区间 有几个）
    # https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=leetcode-75
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
        return ans
    
    # @ 763. 划分字母区间
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = [0] * 27 # hash数组记录每个字符最后出现的位置
        for i in range(len(S)):
            hashmap[ord(S[i]) - ord('a')] = i
        
        result = []
        left, right = 0, 0
        for i in range(len(S)):
            right = max(right, hashmap[ord(S[i]) - ord('a')]) # 找到最远边界
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
    
    # @ 986. 区间列表的交集
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]

            if b2 >= a1 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])

            if b2 < a2:
                j += 1
            else:
                i += 1

        return res
    # 1024.
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        # 按起点升序排列，起点相同的降序排列
        # PS：其实起点相同的不用降序排列也可以，不过我觉得这样更清晰
        clips.sort(key=lambda x: (x[0], -x[1]))
        # 记录选择的短视频个数
        res = 0
        curEnd, nextEnd = 0, 0
        i, n = 0, len(clips)
        while i < n and clips[i][0] <= curEnd:
            # 在第 res 个视频的区间内贪心选择下一个视频
            while i < n and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            # 找到下一个视频，更新 curEnd
            res += 1
            curEnd = nextEnd
            if curEnd >= T:
                # 已经可以拼出区间 [0, T]
                return res
        # 无法连续拼出区间 [0, T]
        return -1
    
    # @ 1288. 删除被覆盖区间 
    # 当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size < 2:
            return size

        intervals.sort(key=lambda x: (x[0], -x[1]))

        remove_count = 0
        max_right = intervals[0][1]

        for i in range(1, size):
            if intervals[i][1] <= max_right:
                remove_count += 1
            else:
                max_right = intervals[i][1]

        return size - remove_count 