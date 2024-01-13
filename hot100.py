class Solution:
    # @ 128 最长连续序列
    def longestConsecutive(self, nums: List[int]) -> int:
        # ? 转化成哈希集合，方便快速查找是否存在某个元素, 没有前驱结点的是连续序列中的开头
        set_num = set(nums)
        res = 0
        for num in set_num:
            if num - 1 in set_num: # :前驱结点不在，则可以判断是 num 是连续子序列的第一个
                continue
            
            cur_num = num # cur_num 是连续子序列的第一个，开始向上计算连续子序列的长度
            cur_len = 1

            while cur_num + 1 in set_num:
                cur_num += 1
                cur_len += 1
            # 更新最长连续序列的长度
            res = max(res, cur_len)

        return res
    # 11 盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxArea=0
        while l < r:
            he = min(height[l], height[r])
            maxArea = max(he * (r-l), maxArea)
            if he == height[l]:
                l+=1
            else:
                r-=1
        return maxArea
    
    # 49 字母异位词分组 思想是，字符串排序之后相等，所以固定使用一个key
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # n 为 3，从 nums[0] 开始计算和为 0 的三元组
        return self.nSumTarget(nums, 3, 0, 0)

    # 注意：调用这个函数之前一定要先给 nums 排序
    # n 填写想求的是几数之和，start 从哪个索引开始计算（一般填 0），target 填想凑出的目标和
    def nSumTarget(self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        sz = len(nums)
        res = []
        # 至少是 2Sum，且数组大小不应该小于 n
        if n < 2 or sz < n:
            return res
        # 2Sum 是 base case
        if n == 2:
            # 双指针那一套操作
            lo, hi = start, sz - 1
            while lo < hi:
                s = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if s < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif s > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            # n > 2 时，递归计算 (n-1)Sum 的结果
            for i in range(start, sz):
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                for arr in sub:
                    # (n-1)Sum 加上 nums[i] 就是 nSum
                    arr.append(nums[i])
                    res.append(arr)
                while i < sz - 1 and nums[i] == nums[i + 1]:
                    i += 1
        return res
    def trap(self, height: List[int]) -> int:
        #左右两边分别 单调栈，记录左右两边的最大高度
        
        n= len(height)
        left, right=[0]*n, [0]*n #两端存不住水
        for i in range(1,n):
            left[i] = max(left[i-1], height[i-1])
        for i in range(n-2,-1,-1):
            right[i] = max(right[i+1], height[i+1])
        
        water = 0
        for i in range(n):
            water+= max(0, min(left[i],right[i])-height[i])
        return water
    
    # 438.找到字符串中所有字母异位词 思想：用长度为26的数组代替字典
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1

        if s_count == p_count:
            ans.append(0)
        # print(s_count,'\n', p_count)
        for i in range(s_len - p_len):
            s_count[ord(s[i]) - ord('a')] -= 1 #左边界
            s_count[ord(s[i + p_len]) - ord('a')] += 1 #右边界
            
            if s_count == p_count:
                ans.append(i + 1)

        return ans
    # 48 旋转图像
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 先沿对角线反转二维矩阵
        for i in range(n):
            for j in range(i, n):
                # swap(matrix[i][j], matrix[j][i]);
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # 然后反转二维矩阵的每一行
        for row in matrix:
            self.reverse(row)
    
    # 反转一维数组
    def reverse(self, arr: List[int]) -> None:
        i, j = 0, len(arr) - 1
        while j > i:
            # swap(arr[i], arr[j]);
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    # 240. 搜索二维矩阵 思想是选择右上角，确保可以选择的方向 是相反的变化
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 初始化在右上角
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                # 需要大一点，往下移动
                i += 1
            else:
                # 需要小一点，往左移动
                j -= 1
        # while 循环中没有找到，则 target 不存在
        return False
    # @ 中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """动态规划思路
        定义：输入一个节点，返回以该节点为根的二叉树的中序遍历结果
        """
        res = []
        if not root:
            return res
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res
        # 主函数
    # @ 226.翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 遍历二叉树，交换每个节点的子节点
        self.traverse(root)
        return root

    # 二叉树遍历函数
    def traverse(self, root: TreeNode) -> None:
        if not root:
            return
        # 前序位置
        # 每一个节点需要做的事就是交换它的左右子节点
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # 遍历框架，去遍历左右子树的节点
        self.traverse(root.left)
        self.traverse(root.right)
    # @ 101 对称二叉树
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)
    
    def majorityElement(self, nums: List[int]) -> int:
        # 我们想寻找的那个众数
        target = 0
        # 计数器（类比带电粒子例子中的带电性）
        count = 0
        for i in range(len(nums)):
            if count == 0:
                # 当计数器为 0 时，假设 nums[i] 就是众数
                target = nums[i]
                # 众数出现了一次
                count = 1
            elif nums[i] == target:
                # 如果遇到的是目标众数，计数器累加
                count += 1
            else:
                # 如果遇到的不是目标众数，计数器递减
                count -= 1
        # 回想带电粒子的例子
        # 此时的 count 必然大于 0，此时的 target 必然就是目标众数
        return target
    # 颜色分类
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0: # 为0，做出决策
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:   # 为2，做出决策
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:                   # 为1，做出决策
                curr += 1

