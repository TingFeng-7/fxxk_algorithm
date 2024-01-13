from typing import List

class Solution:

    #  53. 最大子数组和 (元素连续)
    def maxSubArray(self, nums: List[int]) -> int:
        n, res = len(nums), float('-inf')
        if n == 0:
            return 0
        dp = [0] * n
        # ? 1. base case
        dp[0] = nums[0]
        res = dp[0]
        # ? 2. 状态转移方程
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            # ? 3. 得到 nums的最大子数组和 
            res = max(res, dp[i]) #: not omit
        return res

    # lcr168. 丑数
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        #  if n is Ugly-Number，分解因子应该只有 2, 3, 5
        while n % 2 == 0: n //= 2
        while n % 3 == 0: n //= 3
        while n % 5 == 0: n //= 5
        return n == 1

    # 264 丑数2
    def nthUglyNumber(self, n: int) -> int:
        
        p2, p3, p5 = 1, 1, 1 #: three pointer
        product2, product3, product5 = 1, 1, 1 #: three pointer value
        # 最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 结果链表上的指针
        p = 1
        # 开始合并三个有序链表
        while p <= n: 
            minv = min(product2, product3, product5) #: 取三个链表的最小结点
            # 接到结果链表上
            ugly[p] = minv
            p += 1
            # 前进对应有序链表上的指针
            if minv == product2:
                product2 = 2 * ugly[p2]
                p2 += 1
            if minv == product3:
                product3 = 3 * ugly[p3]
                p3 += 1
            if minv == product5:
                product5 = 5 * ugly[p5]
                p5 += 1
        return ugly[n]

    # -n 最少数目 的 一个问题
    def numSquares(self, n: int) -> int:
        # ! 定义：和为 i 的平方数的最小数量是 dp[i]
        dp = [float('inf')] * (n+1)
        # base case
        dp[0] = 0
        # 状态转移方程
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                # i - j * j 只要再加一个平方数 j * j 即可凑出 i
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        print(dp)
        return dp[n]

    # 322. 零钱兑换
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000] * (amount+1)
        dp[0] = 0
        for tot in range(1, amount+1):
            for coin in coins:
                if tot - coin  < 0:
                    continue
                dp[tot] = min(dp[tot], dp[tot - coin]+1)
        return -1 if dp[amount] == 100000 else dp[amount]

    #  整数拆分  （乘积最大的整数）
    def integerBreak(self, n):
        dp = [0] * (n + 1)   # 创建一个大小为n+1的数组来存储计算结果
        dp[2] = 1  # 初始化dp[2]为1，因为当n=2时，只有一个切割方式1+1=2，乘积为1
        # 从3开始计算，直到n
        for i in range(3, n + 1):
            # 遍历所有可能的切割点
            for j in range(1, i // 2 + 1):
                # 计算切割点j和剩余部分(i-j)的乘积，并与之前的结果进行比较取较大值
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)

        return dp[n]  # 返回最终的计算结

    #  不同的二叉搜索树
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            for j in range(0, i):
                print(f'{dp[j]} * {dp[i-1-j]}')
                dp[i] += dp[j] * dp[i-1-j]  # dp[0] * dp[2]
        return dp[n]
