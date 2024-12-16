# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 此时栈里要放的是pair<节点指针，路径数值>
        st = [(root, root.val)]
        while st:
            node, path_sum = st.pop()
            # 如果该节点是叶子节点了，同时该节点的路径数值等于sum，那么就返回true
            if not node.left and not node.right and path_sum == sum:
                return True
            # 右节点，压进去一个节点的时候，将该节点的路径数值也记录下来
            if node.right:
                st.append((node.right, path_sum + node.right.val))
            # 左节点，压进去一个节点的时候，将该节点的路径数值也记录下来
            if node.left:
                st.append((node.left, path_sum + node.left.val))
        return False


  