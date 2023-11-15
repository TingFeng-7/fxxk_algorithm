from typing import List


class Solution:
    # ! 072 编辑距离
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # dp[i][j] 表示 i长度的word1 到 j长度 的word2 的最少操作数
        for i in range(1, m+1):
            dp[i][0] = i  # 由于 word2长度为 0，所以 操作数等于 word1 减完自己
        for j in range(1, n+1):
            dp[0][j] = j  # 反之由于 word1长度为 0

        # 自底向上求解, 将 word1 转换成 word2 所使用的最少操作数
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,  # insert
                        dp[i][j-1] + 1,  # delete
                        dp[i-1][j-1] + 1  # replace
                    )
        return dp[m][n]  # ? 储存着整个 word1 和 word2 的最小编辑距离

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(0, i):
                # 条件关注
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

            res = max(res, dp[i])  # 子序列，有点子数组的感觉
        return res
