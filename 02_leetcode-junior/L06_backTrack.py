from typing import List, Optional

#  https://labuladong.gitee.io/algo/di-ling-zh-bfe1b/hui-su-sua-56e11/
# hot 100
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        #  22. 括号生成
        #回溯 剪枝
        sz = 2 * n
        res = []
        def dfs(path, l_num, r_num):
            if  l_num > n or r_num > n or r_num > l_num:
                return
            if len(path) == sz and l_num==r_num:
                res.append(path[:])
                return
            # print(l_num, r_num)
            dfs(path+'(', l_num+1, r_num)
            dfs(path+')', l_num, r_num+1)

        dfs("", 0, 0)
        return res 
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        #  46. 全排列
        res, used = [], [False] * len(nums)  # 用访问数组 来禁止访问
        def backtrack(nums, path):
            if not nums: # 如果数组里没有值
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #  47. 全排列 
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        self.backtrack([], nums, check)
        return self.res
    
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #  78.子集
        res, n = [], len(nums)
        
        def backtrack(start:int, path:List[int]):
            if len(path) > n:
                return
            else:
                res.append(path[:])  # : or path.copy()
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i + 1, path)  # @ i+1 不是start+1
                    path.pop(-1)
        backtrack(0, [])
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 39. 组合总和 
        res, n  = [], len(candidates) 
        def backtrack(start, curpath, cursum):  # 开始位置， 上一层选择
            #! 1.结束条件
            if cursum >= target:
                if cursum == target:
                    res.append(curpath.copy())
                return
            #! 2.选择列表
            for i in range(start, n):
                curpath.append(candidates[i])
                cursum += candidates[i]
                backtrack(i, curpath, cursum)
                curpath.pop(-1)
                cursum -= candidates[i]
        backtrack(0, [], 0)
        return res


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 组合总和 3
        res = []
        def backtrack(start, curpath, cursum):  # 开始index， 当前选择， 当前选择和
            if len(curpath) == k:  # 顺利终止条件
                if cursum == n:
                    res.append(curpath.copy())
                    # 因为curpath一直是引用，如果不分离 值一直会改变的
                return
            # for i in range(start, len(nums)):
            # # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            #     if i > start and nums[i] == nums[i-1]:
            #         continue
            # 选择
            for ind in range(start + 1, 10):
                cursum += ind
                curpath.append(ind)
                backtrack(ind, curpath, cursum)
                cursum -= ind
                curpath.pop(-1)

        backtrack(0, [], 0)
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 51 N皇后
        # 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
        # n皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        # 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
        # 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
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
                    on_path[c] = diag1[r + c] = diag2[r - c] = True  # 恢复现场
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False  #  恢复现场
        dfs(0)
        return ans
    
    def letterCombinations(self, digits: str) -> List[str]:
        # @ 17. 电话号码的字符组合
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
        combination = []
        res = []

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
        res = []
        n = len(s)
        def backtrack(start, curpath, cursum):  # 开始位置， 上一层选择
            #! 1.结束条件
            if start == n:
                res.append(curpath.copy())
                return
            #! 2.选择列表
            for i in range(start, n):
                if not self.isPalindrome(s, start, i):
                    continue
                curpath.append(s[start:i+1])
                backtrack(i+1, curpath, cursum)
                curpath.pop(-1)

        backtrack(0, [], 0)
        return res

    # 用双指针技巧判断 s[lo..hi] 是否是一个回文串
    def isPalindrome(self, s: str, lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    
    # @ 113. 路径总和 2  对二叉树
    def pathSum(root, targetSum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, targetSum)
        return res