
from typing import List

# 当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况

# 情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
# 情况二：下标i 与 j相差为1，例如aa，也是文子串
# 情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，
#           我们看i到j区间是不是回文子串就看aba是不是回文就可以了，那么aba的区间就是
#           i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。

# 5. 最长回文子串
def longestPalindrome(s: str) -> str:
    # 二重循环 + 判断是否回文 中心扩散法
    res = ""
    def palindrome(s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        #! 以 s[i] 和 以 s[i] 和 s[i+1]; 为中心的最长回文子串
        s1 = palindrome(s, i, i)
        s2 = palindrome(s, i, i + 1)
        # res = longest(res, s1, s2)
        res = res if len(res) > len(s1) else s1
        res = res if len(res) > len(s2) else s2
    return res

def longestPalindrome_dp(self, s: str) -> str:
    dp=[[False]*len(s) for i in range(len(s))]
    maxL=1
    left,right = 0 ,0
    for i in range(len(s)):
        dp[i][i] =True
    for i in range(len(s)-1,-1,-1): # 自下向上
        for j in range(i, len(s)): # 从左到右
            if (j - i <= 1 or dp[i + 1][j - 1]) and s[i] == s[j]:
                dp[i][j] =True
            if dp[i][j] and j-i+1 > maxL:
                maxL = j-i+1
                left, right = i, j
    return s[left:left+maxL]

def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    res = 1
    for i in range(1, n):  # 终点
        for j in range(0, i):  # 起点
            # 条件关注
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

        res = max(res, dp[i])  # max 循环遍历
    return res

# -n 31.下一个全排列


def nextPermutation(self, nums):
    n = len(nums)
    if n <= 1:
        return

    i = n - 2
    # find: A[i]<A[j]
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        k = n - 1
        # find: A[i]<A[k]
        while nums[k] <= nums[i]:
            k -= 1
        nums[i], nums[k] = nums[k], nums[i]

    # reverse A[j:end]
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
