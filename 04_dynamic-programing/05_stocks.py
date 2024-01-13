from typing import List

# dp[i][k][0 or 1]
# 0 <= i <= n - 1, 1 <= k <= K
# n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票。
# 详细解析参见：
# https://labuladong.github.io/article/?qno=解决方案方法一：暴力法【超时】方法二：一次遍历

class Solution:
    # -n 121. 买卖股票的最佳时机
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
        if n <= 1:
            return 0
        maxVal = 0
        minVal = prices[0]
        for i in range(n):  # ! 其实可以从 1 开始
            maxVal = max(maxVal, prices[i] - minVal)
            minVal = min(minVal, prices[i])
        return maxVal
    # 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]
