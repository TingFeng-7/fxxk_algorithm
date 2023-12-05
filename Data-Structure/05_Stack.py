
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) != 0:
            if self.mins[-1] >= val:
                self.mins.append(val)
        elif len(self.mins) == 0:
            self.mins.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.mins) != 0:
            return self.mins[-1]
        return 0
    
# 括号问题
# https://labuladong.github.io/algo/di-san-zha-24031/jing-dian--a94a0/ru-he-jie--306f6/
class Solution:
    # @ 20 有效的括号 思想：左括号进栈，右括号出现但没有相应左括号是 直接返回false
    def isValid(self, s: str) -> bool:
        hashmap = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in hashmap:
                stack.append(c)
            elif stack != []:  # : 栈不为空的前提下
                if hashmap[stack.pop()] != c:
                    return False
            else: # : 栈已经为空了
                return False
        return stack == []
    
    # 编码字符串
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
    
    # 简化路径
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stk = []
        # 借助栈计算最终的文件夹路径
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stk:
                    stk.pop()
                continue
            stk.append(part)
        # 栈中存储的文件夹组成路径
        res = ""
        while stk:
            res = '/' + stk.pop() + res
        return res if res else '/'