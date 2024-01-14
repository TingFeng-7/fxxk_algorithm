class Solution:
    # @ 7.整数反转
    def reverse(self, x: int) -> int:
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = 1 if x>0 else -1
        x = abs(x)
        while x > 0:
            remain = x % 10
            x = x // 10
            res = res * 10 + remain
        x = res * sign
        return x if INT_MIN < x < INT_MAX else 0
    
    # @ 9.回文数
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        # y 是 x 翻转后的数字
        y = 0
        while temp > 0:
            last_digit = temp % 10
            temp = temp // 10
            # 从最高位生成数字的技巧
            y = y * 10 + last_digit
        return y == x
    
    # @ 12。整数转罗马字符
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0: #如果 nums 能容下这个书
                remain = num // key  # 比如输入4000，remain 为 4
                res += hashmap[key] * remain  # 字符串 叠加 * remain 次
                num %= key
        return res
