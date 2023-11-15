class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def buildTree(nodes, i):
    if i>= len(nodes) or nodes[i] == "#":
        return None
    root = TreeNode(int(nodes[i]))
    root.left = buildTree(nodes, 2*i+1)
    root.right = buildTree(nodes, 2*i+2)
    return root

def levelOrder(root):
    if not root:
        return None
    res = []
    queue = [root]
    tmp_store = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue[i]
            print(node)
            if node.left:
                tmp_store.append(node.left)
            if node.right:
                tmp_store.append(node.right)
            res.append(node.val)
        queue = tmp_store
    return res

tree = input()[1:-1]

print(tree)
print(type(tree))

nodes = tree.split(',')
root = buildTree(nodes, 0)
print(root)

print(levelOrder(root))

