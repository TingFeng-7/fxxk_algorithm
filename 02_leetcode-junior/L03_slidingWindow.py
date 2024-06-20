from typing import List
class Solution:
    # @ 76. 最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        window = Counter()
        left, right = 0, 0
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start, length = 0, float('inf') 
        while right < len(s):
            # ? 1.c是将移入窗口的字符
            c = s[right]
            right += 1
            # ? 2.进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # ? 3.判断左侧窗口是否要收缩
            while valid == len(need): 
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                # d 是将移出窗口的字符
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1 
        # 返回最小覆盖子串
        return '' if length == float('inf') else s[start:start+length]
    
    # @ 3.无重复字符的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = right = 0
        res = 0 # 记录结果
        while right < len(s):
            #? 1.c是将移入窗口的字符
            c = s[right]
            right += 1
            #? 2.进行窗口内数据的一系列更新
            window[c] = window.get(c, 0) + 1
            #? 3.判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1

            res = max(res, right - left)
        return res
    
    # @ 209. 长度最小的子数组
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        left, right = 0, 0
        cursum = 0
        window = []
        while right < n:
            window.append(nums[right])
            cursum += nums[right]
            # 只要当前和超过了s
            while cursum >= s: 
                ans = min(ans, right - left + 1)
                cursum -= nums[left]
                left += 1
            
            right += 1
        
        return 0 if ans == n + 1 else ans