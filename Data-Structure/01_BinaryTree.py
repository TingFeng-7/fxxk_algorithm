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
        if not root: return []
        #根结点入queue
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
    
    # @100. 相同的树 的基础上稍加改动
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """_summary_

        Args:
            p (Optional[TreeNode]): a tree
            q (Optional[TreeNode]): b tree

        Returns:
            bool: _description_
        """        
        if p == None and q == None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and \
            self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left) #两个左对左，现在变左对右
    
    # class Solution {
# public:
#     bool check(TreeNode *p, TreeNode *q) {
#         if (!p && !q) return true;
#         if (!p || !q) return false;
#         return p->val == q->val && check(p->left, q->right) && check(p->right, q->left);
#     }

#     bool isSymmetric(TreeNode* root) {
#         return check(root, root);
#     }
# };

    # @ 101. 对称二叉树
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)
    
    # @ 236. 最近公共祖先 先序遍历，中左右
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ find lowest common ancestor
        
        Args:
            root (TreeNode): root node 
            p (TreeNode): a node
            q (TreeNode): b node
        
        Returns:
            TreeNode: _description_
        """        
        if not root:
            return None
        if root == p or root == q: # case1：p,q 其中一个是根节点
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # case2：left,right都有值 p,q 分居左右两边, 
            return root
        elif not left: # case3：p,q 暂时处在同一边
            return right  # 只有左边找到
        else:
            return left  # 只有右边找到
    
    # ~22.括号生成
    def generateParenthesis(self, n: int) -> List[str]:  # 回溯 + 剪枝
        sz, res = 2*n, []

        def dfs(path, lb_num, rl_num): #lb:left bracket
            if lb_num > n or rl_num > n or rl_num > lb_num:
                return
            if len(path) == sz and lb_num == rl_num:
                res.append(path[:])
                return
            # print(lb_num, rl_num)
            dfs(path+'(', lb_num+1, rl_num)
            dfs(path+')', lb_num, rl_num+1)

        dfs("", 0, 0)
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
