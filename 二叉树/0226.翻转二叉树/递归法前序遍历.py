# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 如果根节点为空，则直接返回None
        if not root:
            return None
        # 交换当前节点的左右子树
        root.left, root.right = root.right, root.left
        # 递归地翻转左子树
        self.invertTree(root.left)
        # 递归地翻转右子树
        self.invertTree(root.right)
        # 返回翻转后的树的根节点
        return root