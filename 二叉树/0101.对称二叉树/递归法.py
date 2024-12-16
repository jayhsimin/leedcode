class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    # 如果根节点为空，说明是对称的
    if not root:
        return True

    # 辅助函数，用来检查左右子树是否对称
    def isSymmetricSubtree(left: TreeNode, right: TreeNode) -> bool:
        # 如果左右子树都为空，说明对称
        if not left and not right:
            return True
        # 如果其中一个为空，另一个不为空，不对称
        if not left or not right:
            return False
        # 如果当前节点的值不同，不对称
        if left.val != right.val:
            return False
        # 递归检查左右子树是否对称
        return isSymmetricSubtree(left.left, right.right) and isSymmetricSubtree(left.right, right.left)
    # left.left 表示当前节点 left 的左子树。
    # right.right 表示当前节点 right 的右子树。


    # 调用辅助函数，检查左右子树是否对称
    return isSymmetricSubtree(root.left, root.right)
# 创建一个对称的二叉树
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

# 创建一个非对称的二叉树
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(4)

# 测试对称的树
print(isSymmetric(root1))  # 输出: True

# 测试非对称的树
print(isSymmetric(root2))  # 输出: False