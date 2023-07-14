class Solution:

    def longestPalindrome(self, s: str) -> str: # 动态规划法
        dp=[[False]*len(s) for i in range(len(s))]
        maxL=1
        left,right = 0 ,0
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] =True
                if dp[i][j] and j-i+1 > maxL:
                    maxL = j-i+1
                    left,right = i, j
        return s[left:left+maxL]
    def longestPalindrome_1(self, s: str) -> str: #二重循环 + 判断是否回文 中心扩散法
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