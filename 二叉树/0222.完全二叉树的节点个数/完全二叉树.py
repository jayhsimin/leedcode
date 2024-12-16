class TreeNode:
    def __init__(self,root=0,right=None,left=None):
        self.root=root
        self.right=right
        self.left=left

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0#遞歸停止條件
        
        left = root.left
        right = root.right
        leftDepth = 0 #这里初始为0是有目的的，为了下面求指数方便
        rightDepth = 0
        while left: #求左子树深度
            left = left.left
            leftDepth += 1
        while right: #求右子树深度
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1 #注意(2<<1) 相当于2^2，所以leftDepth初始为0
        
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# 完全二叉樹的特性：
# 如果左子樹深度與右子樹深度相等，說明這棵樹是 滿二叉樹。
# 滿二叉樹的節點數可以直接用公式計算，而不需要遞歸遍歷所有節點。