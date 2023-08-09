class Solution:
    #072
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # base case
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        
        # 自底向上求解
        # 将 word1 转换成 word2 所使用的最少操作数
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1, # insert
                        dp[i][j-1] + 1, # delete
                        dp[i-1][j-1] + 1 # replace
                    )
        
        # 储存着整个 word1 和 word2 的最小编辑距离
        return dp[m][n]