class Solution:

    def longestPalindrome(self, s: str) -> str:
        #! 动态规划法
        dp = [[False]*len(s) for i in range(len(s))]
        maxL = 1
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j-i+1 > maxL:
                    maxL = j-i+1
                    left, right = i, j
        return s[left:left+maxL]

    # ! 最长回文子串
    def longestPalindrome_1(self, s: str) -> str:
        # -n 二重循环 + 判断是否回文 中心扩散法
        res = ""

        def palindrome(s, l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def countSubstrings(self, s):
        # 动态规划法
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = 0

        for j in range(len(s)):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1

        return ans

    def strStr(self, ss: str, pp: str) -> int:
        n = len(ss)
        m = len(pp)
        s = list(ss)
        p = list(pp)

        # 枚举原串的「发起点」
        for i in range(0, n - m + 1):
            a = i
            b = 0
            # 从原串的「发起点」和匹配串的「首位」开始，尝试匹配
            while b < m and s[a] == p[b]:
                a += 1
                b += 1
            # 如果能够完全匹配，返回原串的「发起点」下标
            if b == m:
                return i
        return -1

    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        n = len(s)
        hashmap = defaultdict()
        l, r = 0, 0
        maxl = 0
        while r < n:
            c = s[r]
            hashmap[c] = hashmap.get(c, 0) + 1
            r += 1
            while hashmap[c] >= 2:  # 收缩条件
                del_char = s[l]
                l += 1
                hashmap[del_char] -= 1
            maxl = max(maxl, r-l)

        return maxl
