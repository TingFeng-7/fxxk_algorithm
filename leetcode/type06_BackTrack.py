from typing import List

class Solution:
    #-n https://leetcode.cn/problems/combination-sum/submissions/
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(start, curpath, cursum): #开始位置， 上一层选择
            #! 1.结束条件
            if cursum>=target:
                if cursum == target:
                    res.append(curpath.copy())
                return
            #! 2.选择列表
            for i in range(start, n):
                curpath.append(candidates[i])
                cursum+= candidates[i]
                backtrack(i, curpath, cursum)
                curpath.pop(-1)
                cursum-= candidates[i]
        backtrack(0,[],0)
        return res
    
    #-n https://leetcode.cn/problems/combination-sum-iii/submissions/
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, curpath, cursum): #开始index， 当前选择， 当前选择和
            if len(curpath) == k:  # 顺利终止条件
                if cursum == n:
                    res.append(curpath.copy())
                    #因为curpath一直是引用，如果不分离 值一直会改变的
                return
            # 选择
            for ind in range(start+1, 10):
                cursum += ind
                curpath.append(ind)
                backtrack(ind, curpath , cursum)
                cursum -= ind
                curpath.pop(-1)

        backtrack(0,[],0)
        return res
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        :type n: int
        :rtype: List[List[str]]
        '''
        m = n * 2 - 1
        ans = []
        col = [0] * n
        on_path, diag1, diag2 = [False] * n, [False] * m, [False] * m
        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
                return
            for c, on in enumerate(on_path):
                if not on and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c
                    on_path[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combination = list()
        res = list()

        def backtrack(index: int):
            if index == len(digits):
                res.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()


        backtrack(0)
        return res
    
    def partition(self, s: str) -> List[List[str]]:
    
        res=[]
        n = len(s)
        
        def backtrack(start, curpath, cursum): #开始位置， 上一层选择
            #! 1.结束条件
            if start==n:
                res.append(curpath.copy())
                return
            #! 2.选择列表
            for i in range(start, n):
                if not self.isPalindrome(s, start, i):
                    continue 
                curpath.append(s[start:i+1])
                backtrack(i+1, curpath, cursum)
                curpath.pop(-1)

        backtrack(0,[],0)
        return res

    # 用双指针技巧判断 s[lo..hi] 是否是一个回文串
    def isPalindrome(self, s: str, lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True