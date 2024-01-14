from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # 左中右 中序遍历
    pre = float('-inf')
    # @ 98. 验证二叉搜索树
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 访问左子树
        if not self.isValidBST(root.left):
            return False
        # 访问当前节点:如果当前节点小于等于中序遍历列表的前一个节点,说明不满足BST,返回 False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        # 访问右子树
        return self.isValidBST(root.right)

    # 二叉搜索树转排序双向链表
    def treeToDoublyList(self, root: Optional[TreeNode]) ->  Optional[TreeNode]:
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        flag = False
        while q:
            tmp = q.pop(0)
            if not tmp:               # 如果当前为空，设置 flag 表示已经遇到空结点了
                flag = True
                continue
            if flag == True:          # 如果当前不为空，且之前有空结点，则必不为完全二叉树
                return False
            q.append(tmp.left)        # 注意此处不判断左右子结点是否为空，而是直接加入队列
            q.append(tmp.right)
        
        return True
    # @ 450. 删除bst的某个节点
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left == None: return root.right
            if root.right == None: return root.left
            tmp = root.left
            while tmp.right != None:
                tmp = tmp.right
            tmp.right = root.right
            return root.left
        elif root.val < key: 
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

    # @ 230. BST中第 k 小元素
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x = [0]
        res = [0]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            x[0] += 1
            cur_val = root.val
            if x[0] == k:
                res[0] = cur_val
                return
            dfs(root.right)
        dfs(root)
        return res[0]