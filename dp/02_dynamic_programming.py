from typing import List

class Solution:

# -n https://leetcode.cn/problems/longest-palindromic-substring/submissions/
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[1] * n
        res = 1
        for i in range(1, n):
            for j in range(0,i):
                # 条件关注
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    #max 里面有自己 
            res = max(res, dp[i])
        return res
# -n 丑数
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        # 如果 n 是丑数，分解因子应该只有 2, 3, 5
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1
    
# -n 丑数2
    def nthUglyNumber(self,n: int) -> int:
        # 三个指向有序链表头结点的指针
        p2,p3,p5 = 1,1,1
        # 三个有序链表的头节点的值
        product2, product3, product5 = 1, 1, 1
        # 最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 结果链表上的指针
        p = 1

        # 开始合并三个有序链表
        while p <= n:
            #! 取三个链表的最小结点
            minv = min(product2, product3, product5)
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

        # 返回第 n 个丑数
        return ugly[n]
    
    #-n 最少数目 的 一个问题
    def numSquares(self, n: int) -> int:
        # 定义：和为 i 的平方数的最小数量是 dp[i]
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
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000] * (amount+1)
        dp[0] = 0
        n = len(coins)
        for i in range(1,amount+1):
            for j in coins:
                if i-j < 0:
                    continue
                dp[i] = min(dp[i],dp[i-j]+1)
        return -1 if dp[amount] == 100000 else dp[amount]