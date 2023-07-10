class Solution:

    def longestPalindrome(self, s: str) -> str:
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