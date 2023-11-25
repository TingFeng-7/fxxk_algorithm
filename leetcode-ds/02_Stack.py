
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


class Solution:
    # -N 有效的括号
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