from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# : 1.遍历题型
class Solution01:
    # @ 199 树的右视图
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return [] #根结点入queue
        queue = [root]
        res = []
        while queue:
            #只需要对该层最后一个元素入列表
            res.append([node.val for node in queue][-1])
            #存储当前层的孩子节点列表
            next_level = []
            #对当前层的每个节点遍历
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = next_level
        return res
    

# : 2. 构造题型
class ConstructTree(object):
	def buildTree(self, preorder, inorder):
		if not (preorder and inorder):
			return None
		# 根据前序数组的第一个元素，就可以确定根节点	
		root = TreeNode(preorder[0])
		# 用preorder[0]去中序数组中查找对应的元素
		mid_idx = inorder.index(preorder[0])
		# 递归的处理前序数组的左边部分和中序数组的左边部分
		# 递归处理前序数组右边部分和中序数组右边部分
		root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
		root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
		return root
