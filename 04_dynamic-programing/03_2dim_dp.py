from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # @ 72 编辑距离
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # definition ： dp[i][j] 表示 i 长度的 word1 到 j长度 的word2 的最少操作数
        for i in range(1, m+1):
            dp[i][0] = i  # 由于 word2 长度为 0，所以 操作数等于 word1 减完自己
        for j in range(1, n+1):
            dp[0][j] = j  # 由于 word1 长度为 0

        # 自底向上求解, 将 word1 转换成 word2 所使用的最少操作数
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]: # 词相等
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1, 
                        dp[i][j-1] + 1,  
                        dp[i-1][j-1] + 1  # replace
                    )
        return dp[m][n]  # ? 储存着整个 word1 和 word2 的最小编辑距离
    # @ 97. 交错字符串
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        n1, n2 = len(s1), len(s2)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        # 我们使用 dpi[j] 表示 s1 的前 个字符和 s2 的前 个字符是否能构成 s 的前+j个字符首先，dp[0][0] 一定是 True
        #base case
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
        
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i-1] and (s2[i-1] == s3[i-1])
        print(dp)
        #dp
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        
        return dp[n1][n2]
    

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(0, i):  # 条件关注
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])  # 子序列，有点子数组的感觉
        return res
