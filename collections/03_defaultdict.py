from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for x in magazine:
            arr[ord(x) - ord('a')] += 1  #* 1.ord()返回字符的ascii
        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1
        return True

    def canConstruct01(self, ransomNote: str, magazine: str) -> bool:
        hashmap = defaultdict(int)  # ? # 哈希表 （带默认值
        for x in magazine:
            hashmap[x] += 1
        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1
        return True

    #~3.无重复最长子串 （滑动窗口）
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = defaultdict()
        l, r, maxl = 0, 0, 0
        while r < n:
            c = s[r]
            hashmap[c] = hashmap.get(c, 0) + 1
            r += 1
            while hashmap[c] >= 2: #?收缩条件,就是这个hash的value要大于2，（有点占空间
                del_ch = s[l]
                l += 1
                hashmap[del_ch] -= 1
            maxl = max(maxl, r-l)
        return maxl

    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        start, maxl = -1, 0 # -1 很微妙
        d = {}  # 元素出现的 位置
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i-start > maxl:
                    maxl = i-start
        return maxl

    #~ 查找第一个字符
    def firstUniqChar(self, s: str) -> int:
        # todo 3. 计数器 统计每个出现的频率
        from collections import Counter
        cnt = Counter(s)
        for idx, ch in enumerate(s):
            if cnt[ch] == 1:
                return idx
        return -1
