from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    pre = float('-inf')
    #~ 有效二叉树
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # 访问左子树
        if not self.isValidBST(root.left):
            return False

        # 访问当前节点:如果当前节点小于等于中序遍历的前一个节点,说明不满足BST,返回 False
        if root.val <= self.pre:
            return False
        
        self.pre = root.val
        
        # 访问右子树
        return self.isValidBST(root.right)