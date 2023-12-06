class Solution:
    # @ 12 整数转罗马字符
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
