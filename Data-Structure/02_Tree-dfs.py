class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# @100. 相同的树  思想：如果左右子树都为空 返回相等， 只有某一个为空则错误， 其余dfs深入返回
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

    
# @ 236. 最近公共祖先 
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

# 22.括号生成
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