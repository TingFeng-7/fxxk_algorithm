from typing import List


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
