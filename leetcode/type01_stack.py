class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack)!= 0:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        elif len(self.minstack)== 0:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack)!= 0:
            return self.minstack[-1]
        return 0
    
class Solution:
    #todo  20
    def isValid(self, s: str) -> bool:
        hashmap = {'{':'}','[':']','(':')'}
        stack = []
        for c in s:
            if c in hashmap:
                stack.append(c)
            elif stack != []: #栈不为空的前提下
                if hashmap[stack.pop()] != c:
                    return False
            else:
                return False
        return stack == []
        