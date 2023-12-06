class Solution:
    # 05.breakpoint 最长回文子串
    def longestPalindrome_dp(self, s: str) -> str:
        #@ 动态规划法
        dp = [[False]*len(s) for i in range(len(s))]
        maxL = 1
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j-i+1 > maxL:
                    maxL = j-i+1
                    left, right = i, j
        return s[left:left+maxL]

    def longestPalindrome_center(self, s: str) -> str:
        # @ 二重循环 + 判断是否回文 中心扩散法
        res = ""
        def palindrome(s, l, r):
            # l,r不越界 and 左右端点相等时
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1 : r]

        for i in range(len(s)):
            s1 = palindrome(s, i, i)  # 以 s[i] 为中心的最长回文子串
            s2 = palindrome(s, i, i + 1) # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            
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

    def strStr(self, ss: str, pp: str) -> int:
        n, m = len(ss), len(pp)
        s, p = list(ss), list(pp)
        # 枚举原串的「发起点」
        for i in range(0, n - m + 1):
            a = i
            b = 0
            # 从原串的「发起点」和匹配串的「首位」开始，尝试匹配
            while b < m and s[a] == p[b]:
                a += 1
                b += 1
            if b == m:             # 如果能够完全匹配，返回原串的「发起点」下标
                return i
        return -1
    
    # 3. 无重复字符最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        n = len(s)
        hashmap = defaultdict()
        l, r = 0, 0
        maxl = 0
        while r < n:
            c = s[r]
            hashmap[c] = hashmap.get(c, 0) + 1
            r += 1
            while hashmap[c] > 1:  # 收缩条件
                del_char = s[l]
                l += 1
                hashmap[del_char] -= 1
            maxl = max(maxl, r-l)
        return maxl

# @ 43 字符串相乘
def multiply(num1: str, num2: str) -> str:
    m, n = len(num1), len(num2) # 结果最多为 m + n 位数
    res = [0] * (m + n) # 从个位数开始逐位相乘
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            intnum1, intnum2= (ord(num1[i]) - ord('0')),  (ord(num2[j]) - ord('0'))
            mul = intnum1 * intnum2 # 乘积在 res 对应的索引位置
            p1, p2 = i + j, i + j + 1 # p1 p2 高位,低位
            sum1 = mul + res[p2] # 当轮乘积 + 当前个位值
            res[p2] = sum1 % 10
            res[p1] += sum1 // 10
    
    i = 0
    while i < len(res) and res[i] == 0: # 越过结果前缀可能存的 0（未使用的位）
        i += 1

    res_str = ''.join(str(e) for e in res[i:]) # 将计算结果转化成字符串
    return res_str if res_str else '0'

# @ 08 字符串转化成整数
def myAtoi(s):
    # 去除前导空格
    s = s.lstrip()

    # 判断正负号
    sign = 1
    if s and (s[0] == '-' or s[0] == '+'):
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    # 读入数字
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # 调整符号并截断结果
    result = sign * result
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    result = max(min(result, INT_MAX), INT_MIN)

    return result

# @ 165 比较版本号
def compareVersion(version1, version2):
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    # 补充版本号长度，使两个版本号长度相同
    while len(v1) < len(v2):
        v1.append(0)
    while len(v2) < len(v1):
        v2.append(0)
    # 逐个比较修订号
    for num1, num2 in zip(v1, v2):
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    return 0

# @ 394. 字符串解码
def decodeString(self, s: str) -> str:
    stack, res, multi = [], "", 0
    for c in s:
        if c == '[':
            stack.append([multi, res])
            res, multi = "", 0
        elif c == ']':
            cur_multi, last_res = stack.pop()
            res = last_res + cur_multi * res
        elif '0' <= c <= '9':
            multi = multi * 10 + int(c)            
        else:
            res += c
    return res



# 示例
version1 = "1.0"
version2 = "1.1"
result = compareVersion(version1, version2)
print(result)
