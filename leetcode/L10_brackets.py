class Solution:
    # 1541
    def minInsertions(self, s: str) -> int:
        res = 0
        need = 0
        
        # Traverse through string s
        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            
            if s[i] == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        
        return res + need
    
    # 921.
    def minAddToMakeValid(self, s: str) -> int:
        res = 0 # res 记录需要左括号的插入次数
        need = 0 # need 变量记录右括号的需求量

        for i in range(len(s)):
            if s[i] == '(':
                # 对右括号的需求 + 1
                need += 1
            elif s[i] == ')':
                # 对右括号的需求 - 1
                need -= 1
                if need == -1:
                    need = 0
                    # 需插入一个左括号
                    res += 1
        
        return res + need